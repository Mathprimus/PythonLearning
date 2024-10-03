import os
import xml.etree.ElementTree as ET
from tkinter import Tk
from tkinter.filedialog import askopenfilename


def verificar_xml(arquivo):
    if os.path.splitext(arquivo)[-1].lower() != '.xml':
        return "O arquivo selecionado não é um XML."

    print('O arquivo é um xml')

    try:
        tree = ET.parse(arquivo)
        root = tree.getroot()

        namespaces = {'nfe': 'http://www.portalfiscal.inf.br/nfe'}

        nNF = root.find('.//nfe:nNF', namespaces)

        if nNF is not None:
            return f"Campo <nNF> encontrado, valor: {nNF.text}"
        else:
            return "Campo <nNF> não encontrado."
    except ET.ParseError:
        return "Erro ao parsear o arquivo XML."


def selecionar_arquivo():
    root = Tk()
    root.withdraw()
    arquivo_selecionado = askopenfilename(title="Selecione o arquivo XML", filetypes=[("Arquivos XML", "*.xml")])
    return arquivo_selecionado


arquivo = selecionar_arquivo()
if arquivo:
    resultado = verificar_xml(arquivo)
    print(resultado)
else:
    print("Nenhum arquivo selecionado.")
