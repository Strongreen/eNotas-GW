import requests
import json



class notaFiscalServico:
  
  def notaFiscalS(self,idExterno,ambienteEmissao, enviarPorEmail, tipoPessoa, nome, email, telefone, cpfCnpj, uf, cidade, logradouro, numero, complemento, bairro,cep, descricao, aliquotaIss, issRetidoFonte, SMU,valorTotal):

    #Colocar algumas tratativas

    if enviarPorEmail == 'true':
      enviarPorEmail = True
    else:
      enviarPorEmail = False

    if issRetidoFonte == 'true':
      issRetidoFonte = True
    else:
      issRetidoFonte = False

    
    if tipoPessoa == 'PF':
      cpfCnpj = cpfCnpj[11:11]
    else:
      cpfCnpj = cpfCnpj[14:14]
    
    uf = uf[:2]

    nfse = {
      "idExterno": idExterno,
      "ambienteEmissao": ambienteEmissao,
      "enviarPorEmail": enviarPorEmail,
      "cliente": {
          "tipoPessoa": tipoPessoa,
          "nome": nome,
          "email": email,
          "telefone": telefone,
          "cpfCnpj": cpfCnpj,
          "endereco": {
              "uf": uf,
              "cidade": cidade,
              "logradouro": logradouro,
              "numero": numero,
              "complemento": complemento,
              "bairro": bairro,
              "cep": cep
          }
      },
    "servico":{
        "descricao": descricao,
        "aliquotaIss": float(aliquotaIss),
        "issRetidoFonte": issRetidoFonte,
        "valorCofins": 0.00,
        "valorCsll": 0.00,
        "valorInss": 0.00,
        "valorIr": 0.00,
        "valorPis": 0.00,
        "codigoInternoServicoMunicipal": int(SMU)
    },
      "valorTotal": float(valorTotal),
      "observacoes": "Essa nota não tem valor fiscal, NOTA DE TESTE"
      }

    return nfse

  def Emite(self,nfse):
    APIKEY = 'APIKey'
    Empresa_ID = 'teste'

    url = "https://api.enotasgw.com.br/v1/empresas/" + Empresa_ID + "/nfs-e"

    payload = json.dumps(nfse) 

    headers = {
      'accept': "application/json",
      'content-type': "application/json",
      'authorization': "Basic " + APIKEY
    }

    response = requests.request("POST", url, data=payload, headers=headers)

    print(response.text)


