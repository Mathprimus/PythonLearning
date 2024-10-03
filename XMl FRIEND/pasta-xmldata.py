import os
import shutil
import xml.etree.ElementTree as ET
from tkinter import Tk
from tkinter.filedialog import askopenfilename
from datetime import datetime

def verificar_xml(arquivo):
    if os.path.splitext(arquivo)[-1].lower() != '.xml':
        return 'Arquivo não é um xml'

    try:
        tree = ET.parse(arquivo)
        root = tree.getroot()

        if root.tag == 'CFe':
            data = root.find('.//ide/dEmi')
            if data is not None:
                salvar_arquivo(data.text, arquivo)
                return f'Data: {data.text}'
            else:
                return 'Data não encontrada.'

        else:
            namespaces = {'nfe': 'http://www.portalfiscal.inf.br/nfe'}
            data = root.find('.//nfe:ide/nfe:dhEmi', namespaces)
            if data is not None:
                salvar_arquivo(data.text, arquivo)
                return f'Data: {data.text}'
            else:
                return 'Data não encontrada.'

    except ET.ParseError:
        return 'Erro ao parsear o arquivo XML.'
    except FileNotFoundError:
        return 'Arquivo não encontrado.'
    except Exception as e:
        return f'Um erro ocorreu: {e}'

def salvar_arquivo(data, arquivo_origem):
    data_obj = datetime.fromisoformat(data)
    data_formatada = data_obj.strftime("%Y%m")

    pasta_data = os.path.join('C:\\Users\\Matheus\\Documents\\XML FRIEND\\teste\\13479490000100', data_formatada)

    if not os.path.exists(pasta_data):
        os.makedirs(pasta_data)
        print(f'Pasta {data_formatada} criada.')

    nome_arquivo = os.path.basename(arquivo_origem)
    caminho_arquivo_destino = os.path.join(pasta_data, nome_arquivo)

    print(f'Tentando salvar o arquivo em: {caminho_arquivo_destino}')

    if not os.path.exists(caminho_arquivo_destino):
        shutil.copy(arquivo_origem, caminho_arquivo_destino)
        print(f'Arquivo copiado para a pasta {data_formatada}.')
    else:
        print(f'O arquivo já existe na pasta {data_formatada}.')

def selecionar_arquivo():
    root = Tk()
    root.withdraw()
    arquivo_selecionado = askopenfilename(title='Selecionar o arquivo xml', filetypes=[('XML Files', '*.xml')])
    return arquivo_selecionado

arquivo = selecionar_arquivo()
if arquivo:
    resultado = verificar_xml(arquivo)
    print(resultado)
else:
    print('Nenhum arquivo foi selecionado')
