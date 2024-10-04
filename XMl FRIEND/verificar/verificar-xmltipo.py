import os
import xml.etree.ElementTree as ET
from tkinter import Tk
from tkinter.filedialog import askopenfilename


def verificar_xml(arquivo):
    if os.path.splitext(arquivo)[-1].lower() != '.xml':
        return 'o arquivo não é um xml',False

    print('O arquivo é um XML.')

    try:
        tree = ET.parse(arquivo)
        root = tree.getroot()

        mod_nfe = root.find('.//{http://www.portalfiscal.inf.br/nfe}mod')
        mod_nfce = root.find('.//{http://www.portalfiscal.inf.br/nfe}mod')

        if mod_nfe is not None and mod_nfe.text == '55':
          return "Documento identificado como NFe."

        elif mod_nfce is not None and mod_nfce.text == '65':
          return 'Documento identificado como NFC-e.'

        cfe = root.find('.//infCFe')
        if cfe is not None:
            return 'Documento identificado como SAT.'

        return 'Tipo de documento não identificado'

    except ET.ParseError:
        return "Erro ao verificar o arquivo"

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
    print('Nenhum arquivo valido selecionado')
