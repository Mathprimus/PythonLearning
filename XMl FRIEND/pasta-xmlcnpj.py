import os
import shutil
import xml.etree.ElementTree as ET
from tkinter import Tk
from tkinter.filedialog import askopenfilename

def verificar_xml(arquivo):
    if os.path.splitext(arquivo)[-1].lower() != '.xml':
        return 'Arquivo não é um XML'

    try:
        tree = ET.parse(arquivo)
        root = tree.getroot()

        if root.tag == 'CFe':
            cnpj = root.find('.//emit/CNPJ')
            salvar_arquivo(cnpj.text, arquivo)
        else:
            namespaces = {'nfe': 'http://www.portalfiscal.inf.br/nfe'}
            cnpj = root.find('.//nfe:emit/nfe:CNPJ', namespaces)
            salvar_arquivo(cnpj.text, arquivo)

        if cnpj is not None:
            return f'CNPJ: {cnpj.text}'
        else:
            return 'CNPJ não encontrado'

    except ET.ParseError:
        return 'Erro ao parsear o arquivo XML.'
    except FileNotFoundError:
        return 'Arquivo não encontrado.'
    except Exception as e:
        return f'Um erro ocorreu: {e}'


def salvar_arquivo(cnpj, arquivo_origem):
    pasta_cnpj = os.path.join('C:\\Users\\Matheus\\Documents\\XML FRIEND\\teste', cnpj)

    if not os.path.exists(pasta_cnpj):
        os.makedirs(pasta_cnpj)
        print(f'Pasta{cnpj} criada')

        nome_arquivo = os.path.basename(arquivo_origem)
        caminho_arquivo_destino = os.path.join(pasta_cnpj, nome_arquivo)

        print(f'Tentando salvar o arquivo em: {caminho_arquivo_destino}')

        if not os.path.exists(caminho_arquivo_destino):
            shutil.copy(arquivo_origem, caminho_arquivo_destino)
            print(f'Arquivo copiado para a pasta {cnpj}')
        else:
            print(f'O arquivo ja existe na pasta {cnpj}')

def selecionar_arquivo():
    root = Tk()
    root.withdraw()
    arquivo_selecionado = askopenfilename(title='Selecionar o arquivo XML', filetypes=[('XML Files', '*.xml')])
    return arquivo_selecionado

arquivo = selecionar_arquivo()
if arquivo:
    resultado = verificar_xml(arquivo)
    print(resultado)
else:
    print('Nenhum arquivo selecionado')