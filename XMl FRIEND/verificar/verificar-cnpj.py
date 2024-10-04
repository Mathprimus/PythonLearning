import os
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
        else:
            namespaces = {'nfe': 'http://www.portalfiscal.inf.br/nfe'}
            cnpj = root.find('.//nfe:emit/nfe:CNPJ', namespaces)

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