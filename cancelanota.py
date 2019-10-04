import requests
import json

# LEIA ESSAS INSTRUÇÕES ANTES DE EXECUTAR O SCRIPT
# Inserir a API Key da Empresa cadastrada no GW
#Instruções de Utilização para cancelar nota em massa
# Criar uma planilha com 2 colunas
# A primeira coluna com os IDs das empresas ( Nomear assim: Empresa_ID)
# Segunda Coluna com os IDs das notas relacionados aquela empresa ( Nomear assim: ID_Nota)
# Salvar a planilha como .csv
# Converter a planilha neste site: http://www.convertcsv.com/csv-to-json.htm
# Step 1: Select your input > Choose File
# Salvar o arquivo json com o nome: cancelar-nota.json
# Executar este SCRIPT

with open('cancelar-nota.json', encoding="UTF-8") as g:
    data = json.load(g)

APIKEY = 'INSERIR A API KEY DA EMPRESA'

for obj in data:

    url = "https://api.enotasgw.com.br/v1/empresas/" + str(obj['Empresa_ID']) + "/nfes/porIdExterno/" + str(obj['ID_Nota'])


    headers = {
      'accept': "application/json",
      'authorization': "Basic " + APIKEY
    }

    response = requests.request("DELETE", url, headers=headers)

    print(response.text)
