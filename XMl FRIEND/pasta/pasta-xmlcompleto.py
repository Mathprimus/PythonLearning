import os
import xml.etree.ElementTree as ET
from tkinter import Tk
from tkinter.filedialog import askopenfilename
import shutil
from datetime import datetime


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
    pasta_cnpj = os.path.join('C:\\Users\\Matheus\\Documents\\XML FRIEND\\teste', cnpj)

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


def selecionar_arquivo():
    root = Tk()
    root.withdraw()
    arquivo_selecionado = askopenfilename(title='Selecionar o arquivo XML', filetypes=[('XML Files', '*.xml')])
    return arquivo_selecionado


arquivo = selecionar_arquivo()
if arquivo:
    mensagem, status = verificar_xml(arquivo)
    print(mensagem)
else:
    print('Nenhum arquivo válido selecionado')
