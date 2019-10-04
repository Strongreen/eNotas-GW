import requests
import json


#Date = dict()
#from pprint import pprint
with open('JSON_retorno.json', encoding="UTF-8") as g:
    data = json.load(g)
cont = 0 
for x in data:
  cont += 1
  if  x['cliente']['endereco']['uf'] == 'PR':
    cfop = '1102'
  else:
    cfop = '2102' 
  
  nfe = {
    "id": "devolucaoteste" + str(cont),
    "ambienteEmissao": "Homologacao",
    "naturezaOperacao": "Devolução",
    "tipoOperacao": "Entrada",
    "nfeReferenciada": [{
        "chaveAcesso": x['chaveAcesso']
    }],
    "finalidade": "DevolucaoMercadoria",
    "consumidorFinal": True,
    "indicadorPresencaConsumidor": "OperacaoPelaInternet",
    "cliente": {
        "tipoPessoa": "F",
        "indicadorContribuinteICMS": "NaoContribuinte",
        "nome": x['cliente']['nome'],
        "email": x['cliente']['email'],
        "telefone": x['cliente']['telefone'],
        "cpfCnpj": x['cliente']['cpfCnpj'],
        "endereco": {
            "uf": x['cliente']['endereco']['uf'],
            "cidade": x['cliente']['endereco']['cidade'],
            "logradouro": x['cliente']['endereco']['logradouro'],
            "numero": x['cliente']['endereco']['numero'],
            "complemento": x['cliente']['endereco']['complemento'],
            "bairro": x['cliente']['endereco']['bairro'],
            "cep": x['cliente']['endereco']['cep']
        }
    },
    "enviarPorEmail": True,
    "itens":[{
        "cfop": cfop,
        "codigo": x['itens'][cont]['codigo'],
        "descricao": x['itens'][cont]['descricao'],
        "ncm": "49019900",
        "quantidade": x['itens'][cont]['quantidade'],
        "unidadeMedida": "UN",
        "valorUnitario": x['itens'][cont]['valorUnitario'],
        "impostos": {
            "icms": {
              "situacaoTributaria": "300",
              "origem": 0
            },
            "pis": {
              "situacaoTributaria": "98" 
            },
            "cofins": {
              "situacaoTributaria": "98" 
            },
            "ipi": {
              "situacaoTributaria": "54",
              "codigoEnquadramento": "001",
              }
          }
        }],
      "informacoesAdicionais": "Documento emitido por ME ou EPP optante pelo Simples Nacional. Não gera direito a crédito fiscal de IPI."
    }


  APIKEY = 'Inserir A api Key'
  Empresa_ID = 'ID da empresa'

  url = "https://api.enotasgw.com.br/v2/empresas/" + Empresa_ID + "/nf-e"

  payload = json.dumps(nfe) 
  
  # Modelo do payload
  
  # "{\"nfe\":{\"id\":\"452121\",\"ambienteEmissao\":\"Homologacao\",\"naturezaOperacao\":\"Venda\",\"finalidade\":\"Normal\",\"consumidorFinal\":true,\"indicadorPresencaConsumidor\":\"OperacaoPelaInternet\",\"cliente\":{\"tipoPessoa\":\"F\",\"indicadorContribuinteICMS\":\"NaoContribuinte\",\"nome\":\"Jonathan Souza\",\"email\":\"jonathan.souza@mail.com\",\"telefone\":\"31987897898\",\"cpfCnpj\":\"10330557270\",\"endereco\":{\"uf\":\"MG\",\"cidade\":\"Belo Horizonte\",\"logradouro\":\"Rua 01\",\"numero\":\"112\",\"complemento\":\"AP 402\",\"bairro\":\"Savassi\",\"cep\":\"32323111\"}},\"enviarPorEmail\":true,\"itens\":[{\"cfop\":\"5101\",\"codigo\":\"1\",\"descricao\":\"string\",\"ncm\":\"38151210\",\"quantidade\":1,\"unidadeMedida\":\"UN\",\"valorUnitario\":1,\"impostos\":{\"icms\":{\"situacaoTributaria\":\"102\",\"origem\":0},\"pis\":{\"situacaoTributaria\":\"07\"},\"cofins\":{\"situacaoTributaria\":\"07\"}}}],\"informacoesAdicionais\":\"I - Documento emitido por ME ou EPP optante pelo Simples Nacional.\\r\\n II - Não gera direito a crédito fiscal de ICMS, de ISS e de IPI.\"}}"
  headers = {
      'accept': "application/json",
      'content-type': "application/json",
      'authorization': "Basic " + APIKEY
      }



  response = requests.request("POST", url, data=payload, headers=headers)

print(response.text)
