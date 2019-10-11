import uuid	
from urllib.request import Request, urlopen
from urllib.error import HTTPError
from io import BytesIO
import codecs

class multiPartRequest:
  def __init__(self, body, contentType):
    self.body = body
    self.contentType = contentType
    

class fileParameter:
  def __init__(self, name, path, contentType):
    self.name = name
    self.rawData = open(path, "rb").read()
    self.contentType = contentType
    

class multipartFormDataEncoder:
  __notAllowedChars = ["\0", "\"", "\r", "\n"]
  __utf8Codec = codecs.lookup('utf-8')[3]
  
  def encode(self, data):
    boundary = "---------------------" + uuid.uuid4().hex
    contentType = 'multipart/form-data; boundary=' + boundary
    bodyStream = BytesIO()
	
    for key in data:
      name = self.removeNotAllowedChars(key)
      value = data[key]
      self.__utf8Codec(bodyStream).write("--" + boundary + "\r\n")
      
      if type(value) is fileParameter:
        self.appendFileParameter(name, value, bodyStream)
      else:
        self.appendParameter(name, value, bodyStream)
        
    self.__utf8Codec(bodyStream).write("--" + boundary + "--")
	  
    return multiPartRequest(bodyStream.getvalue(), contentType)
  
  def removeNotAllowedChars(self, name):
    for c in self.__notAllowedChars:
      name = name.replace(c, "_")
    
    return name
  
  
  def appendParameter(self, name, value, bodyStream):
    self.__utf8Codec(bodyStream).write("Content-Disposition: form-data; name=\"{0}\"".format(name))
    self.__utf8Codec(bodyStream).write("\r\n\r\n")
    self.__utf8Codec(bodyStream).write(value)
    self.__utf8Codec(bodyStream).write("\r\n")
	
  def appendFileParameter(self, name, file, bodyStream):
    self.__utf8Codec(bodyStream).write("Content-Disposition: form-data; name=\"{0}\"; filename=\"{1}\"".format(name, file.name))
    self.__utf8Codec(bodyStream).write("\r\n")
    self.__utf8Codec(bodyStream).write("Content-Type: " + (file.contentType if file.contentType else "application/octet-stream"))
    self.__utf8Codec(bodyStream).write("\r\n\r\n")
    bodyStream.write(file.rawData)
    self.__utf8Codec(bodyStream).write("\r\n")
    
encoder = multipartFormDataEncoder()
  
multipartForm = encoder.encode({
  "arquivo": fileParameter("mycert.pfx", "MyCertFile.pfx", "application/x-pkcs12"),
  "senha": "mypassword"
})
    
empresaId = "{empresaId}"
url = "http://api.enotasgw.com.br/v1/empresas/{0}/certificadoDigital".format(empresaId)

headers = {
  "User-Agent": "MyUserAgent",
  "Accept": "application/json",
  "Authorization": "Basic {Api Key}",
  "Content-Type": multipartForm.contentType
}
  
request = Request(url, headers=headers, method="POST", data=multipartForm.body)

responseText = "<EMPTY>"

try:
	responseStream = urlopen(request).read()
	responseText = responseStream.decode("utf-8")
except HTTPError as ex:
	responseText = ex.fp.read().decode("utf-8")

print(responseText)