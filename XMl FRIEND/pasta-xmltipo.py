import os
import shutil
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

        if mod_nfe is not None and mod_nfe.text == '55':
          tipo = 'NFe'
          salvar_arquivo(tipo, arquivo)
          return "Documento identificado como NFe."


        elif mod_nfe is not None and mod_nfe.text == '65':
          tipo = 'NFC-e'
          salvar_arquivo(tipo, arquivo)
          return 'Documento identificado como NFC-e.'

        cfe = root.find('.//infCFe')
        if cfe is not None:
            tipo = 'sat'
            salvar_arquivo(tipo, arquivo)
            return 'Documento identificado como SAT.'

        return 'Tipo de documento não identificado'
    except ET.ParseError:
        return "Erro ao verificar o arquivo"

def salvar_arquivo(tipo, arquivo_origem):
    pasta_tipo = os.path.join('C:\\Users\\Matheus\\Documents\\XML FRIEND\\teste\\13479490000100\\201812', tipo)

    if not os.path.exists(pasta_tipo):
        os.makedirs(pasta_tipo)
        print(f'Pasta {tipo} criada')

        nome_arquivo = os.path.basename(arquivo_origem)
        caminho_arquivo_destino = os.path.join(pasta_tipo, nome_arquivo)

        print(f'Tentando salvar o arquivo em: {caminho_arquivo_destino}')

        if not os.path.exists(caminho_arquivo_destino):
            shutil.copy(arquivo_origem, caminho_arquivo_destino)
            print(f'Arquivo copiado para a pasta {tipo}')
        else:
            print(f'O arquivo ja existe na pasta {tipo}')

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
