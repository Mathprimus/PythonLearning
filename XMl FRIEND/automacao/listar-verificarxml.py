import os
import time
import xml.etree.ElementTree as ET
import shutil
from datetime import datetime
import configparser

def verificar_xml(arquivo):
    if os.path.splitext(arquivo)[-1].lower() != '.xml':
        return 'O arquivo não é um XML', False

    print('O arquivo é um XML.')

    try:
        tree = ET.parse(arquivo)
        root = tree.getroot()

        mod_nfe = root.find('.//{http://www.portalfiscal.inf.br/nfe}mod')

        if root.tag == 'CFe':
            cnpj = root.find('.//emit/CNPJ').text
            data = root.find('.//ide/dEmi').text
            tipo_documento = "CFE"
        else:
            namespaces = {'nfe': 'http://www.portalfiscal.inf.br/nfe'}
            cnpj = root.find('.//nfe:emit/nfe:CNPJ', namespaces).text
            data = root.find('.//nfe:ide/nfe:dhEmi', namespaces).text

            if mod_nfe is not None and mod_nfe.text == '55':
                tipo_documento = "NFE"
            elif mod_nfe is not None and mod_nfe.text == '65':
                tipo_documento = "NFC-E"
            else:
                return 'Tipo de documento não identificado', False

        salvar_arquivo(cnpj, data, tipo_documento, arquivo)
        return f"Documento {tipo_documento} processado.", True

    except ET.ParseError:
        return "Erro ao verificar o arquivo", False

    except Exception as e:
        return f"Ocorreu um erro: {str(e)}", False


def salvar_arquivo(cnpj, data, tipo_documento, arquivo_origem):
    diretorio_salvar = carregar_caminho_ini('diretorio_salvar')

    if not diretorio_salvar:
        print("Caminho do diretório para salvar não encontrado no config.ini!")
        return

    pasta_cnpj = os.path.join(diretorio_salvar, cnpj)

    if not os.path.exists(pasta_cnpj):
        os.makedirs(pasta_cnpj)
        print(f'Pasta {cnpj} criada.')

    data_obj = datetime.fromisoformat(data)
    data_formatada = data_obj.strftime("%Y%m")

    pasta_data = os.path.join(pasta_cnpj, data_formatada)

    if not os.path.exists(pasta_data):
        os.makedirs(pasta_data)
        print(f'Pasta {data_formatada} criada dentro da pasta {cnpj}.')

    pasta_tipo = os.path.join(pasta_data, tipo_documento)

    if not os.path.exists(pasta_tipo):
        os.makedirs(pasta_tipo)
        print(f'Pasta {tipo_documento} criada dentro da pasta {data_formatada}.')

    nome_arquivo = os.path.basename(arquivo_origem)
    caminho_arquivo_destino = os.path.join(pasta_tipo, nome_arquivo)

    if not os.path.exists(caminho_arquivo_destino):
        shutil.copy(arquivo_origem, caminho_arquivo_destino)
        print(f'Arquivo copiado para a pasta {tipo_documento}.')
    else:
        print(f'O arquivo já existe na pasta {tipo_documento}.')


def listar_arquivos(diretorio):
    print(f"Listando arquivos no diretório: {diretorio}")
    try:
        for dirpath, dirnames, filenames in os.walk(diretorio):
            for arquivo in filenames:
                if arquivo.lower().endswith(".xml"):
                    caminho_completo = os.path.join(dirpath, arquivo)
                    print(f"Arquivo XML encontrado: {caminho_completo}")

                    mensagem, status = verificar_xml(caminho_completo)
                    print(mensagem)

    except FileNotFoundError:
        print("Diretório não encontrado.")
    except Exception as e:
        print(f"Erro ao listar arquivos: {e}")


def monitorar_diretorio(diretorio, intervalo=5):
    while True:
        listar_arquivos(diretorio)
        time.sleep(intervalo)


def salvar_caminho_ini(campo, caminho):
    config = configparser.ConfigParser()
    config['Configuracoes'] = {campo: caminho}

    with open('config.ini', 'w') as configfile:
        config.write(configfile)


def carregar_caminho_ini(campo):
    config = configparser.ConfigParser()
    config.read('config.ini')

    if 'Configuracoes' in config and campo in config['Configuracoes']:
        return config['Configuracoes'][campo]
    else:
        return None


caminho_diretorio_monitorar = carregar_caminho_ini('diretorio_monitorar')
if not caminho_diretorio_monitorar:
    caminho_diretorio_monitorar = input("Digite o caminho do diretório para monitorar: ")
    salvar_caminho_ini('diretorio_monitorar', os.path.normpath(caminho_diretorio_monitorar))
else:
    print(f"Caminho de monitoramento salvo encontrado: {caminho_diretorio_monitorar}")

caminho_diretorio_salvar = carregar_caminho_ini('diretorio_salvar')
if not caminho_diretorio_salvar:
    caminho_diretorio_salvar = input("Digite o caminho do diretório para salvar: ")
    salvar_caminho_ini('diretorio_salvar', os.path.normpath(caminho_diretorio_salvar))
else:
    print(f"Caminho de salvamento salvo encontrado: {caminho_diretorio_salvar}")

monitorar_diretorio(caminho_diretorio_monitorar)
