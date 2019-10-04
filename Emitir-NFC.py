import requests
import json

with open('date.json', encoding="utf8") as g:
    data = json.load(g)

for x in data:

  if  x['estado'] == 'PR':
    cfop = '1202'
  else:
    cfop = '2202' 
  
  nfe = {
    "id": x['id'],
    "ambienteEmissao": "Producao",
    "naturezaOperacao": "Devolução",
    "tipoOperacao": "Entrada",
    "nfeReferenciada": [{
        "chaveAcesso": x['chaveAcesso']
    }],
    "finalidade": "DevolucaoMercadoria",
    "consumidorFinal": True,
    "indicadorPresencaConsumidor": "OperacaoPresencial",
    "cliente": {
        "tipoPessoa": "F",
        "indicadorContribuinteICMS": "NaoContribuinte",
        "nome": x['nome'],
        "email": x['email'],
        "telefone": x['DDD'] and x['telefone'],
        "cpfCnpj": x['cpfCnpj'],
        "endereco": {
            "uf": x['estado'],
            "cidade": x['cidade'],
            "logradouro": x['logradouro'],
            "numero": x['numero'],
            "complemento": x['complemento'],
            "bairro": x['bairro'],
            "cep": x['cep']
        }
    },
    "enviarPorEmail": True,
    "itens":[{
        "cfop": cfop,
        "codigo": x['codigo'],
        "descricao": x['descricao'],
        "ncm": "49019900",
        "quantidade": x['quantidade'],
        "unidadeMedida": "UN",
        "valorUnitario": x['valorUnitario'],
        "impostos": {
          "percentualAproximadoTributos": {
              "simplificado": {
                  "percentual": 31.45
                },
              "fonte": "IBPT"
            },
            "icms": {
              "situacaoTributaria": "102",
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
