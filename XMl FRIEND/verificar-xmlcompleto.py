import os
import xml.etree.ElementTree as ET
from tkinter import Tk
from tkinter.filedialog import askopenfilename


def verificar_xml(arquivo):
    if os.path.splitext(arquivo)[-1].lower() != '.xml':
        return 'O arquivo não é um XML', False

    print('O arquivo é um XML.')

    try:
        tree = ET.parse(arquivo)
        root = tree.getroot()

        mod_nfe = root.find('.//{http://www.portalfiscal.inf.br/nfe}mod')

        if root.tag == 'CFe':
            cnpj = root.find('.//emit/CNPJ')
            data = root.find('.//ide/dEmi')
        else:
            namespaces = {'nfe': 'http://www.portalfiscal.inf.br/nfe'}
            cnpj = root.find('.//nfe:emit/nfe:CNPJ', namespaces)
            data = root.find('.//nfe:ide/nfe:dhEmi', namespaces)

        if cnpj is not None:
            print(f'CNPJ: {cnpj.text}'), True
        else:
            print('CNPJ não encontrado'), False

        if data is not None:
            print(f'Data: {data.text}'), True
        else:
            print('Data não encontrada'), False

        if mod_nfe is not None and mod_nfe.text == '55':
            return "Documento identificado como NFe.", True

        elif mod_nfe is not None and mod_nfe.text == '65':
            return 'Documento identificado como NFC-e.', True

        cfe = root.find('.//infCFe')
        if cfe is not None:
            return 'Documento identificado como SAT.', True

        return 'Tipo de documento não identificado', False

    except ET.ParseError:
        return "Erro ao verificar o arquivo", False

    except Exception as e:
        return f"Ocorreu um erro: {str(e)}", False


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
