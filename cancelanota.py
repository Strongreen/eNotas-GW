import requests
import json

with open('notas-canceladas.json', encoding="UTF-8") as g:
    data = json.load(g)

APIKEY = 'MzEwMzdmOTctY2E5Ni00NDkzLWIxYTUtNTcwZGJmNDcwMTAw'


for obj in data:

    url = "https://api.enotasgw.com.br/v1/empresas" + str(obj['Empresa_ID']) + "/nfes/porIdExterno" + str(obj['ID_Nota'])


    headers = {
      'accept': "application/json",
      'authorization': "Basic " + APIKEY
    }

  response = requests.request("DELETE", url, headers=headers)

    print(response.text)