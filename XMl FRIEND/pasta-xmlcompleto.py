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
            cnpj = root.find('.//emit/CNPJ')
            salvar_cnpj(cnpj.text, arquivo)
            data = root.find('.//ide/dEmi')
            salvar_data(data.text, arquivo)
        else:
            namespaces = {'nfe': 'http://www.portalfiscal.inf.br/nfe'}
            cnpj = root.find('.//nfe:emit/nfe:CNPJ', namespaces)
            data = root.find('.//nfe:ide/nfe:dhEmi', namespaces)
            salvar_cnpj(cnpj.text, arquivo)
            salvar_data(data.text, arquivo)

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

def salvar_cnpj(cnpj, arquivo_origemcnpj):
    pasta_cnpj = os.path.join('C:\\Users\\Matheus\\Documents\\XML FRIEND\\teste', cnpj)

    if not os.path.exists(pasta_cnpj):
        os.makedirs(pasta_cnpj)
        print(f'Pasta{cnpj} criada')

        nome_arquivocnpj = os.path.basename(arquivo_origemcnpj)
        caminho_arquivo_destinocnpj = os.path.join(pasta_cnpj, nome_arquivocnpj)

        print(f'Tentando salvar o arquivo em: {caminho_arquivo_destinocnpj}')

        if not os.path.exists(caminho_arquivo_destinocnpj):
            shutil.copy(arquivo_origemcnpj, caminho_arquivo_destinocnpj)
            print(f'Arquivo copiado para a pasta {cnpj}')
        else:
            print(f'O arquivo ja existe na pasta {cnpj}')

def salvar_data(data, arquivo_origemdata):
    data_obj = datetime.fromisoformat(data)
    data_formatada = data_obj.strftime("%Y%m")
    pasta_data = os.path.join('C:\\Users\\Matheus\\Documents\\XML FRIEND\\teste', data)

    if not os.path.exists(pasta_data):
        os.makedirs(pasta_data)
        print(f'Pasta {data_formatada} criada')

    nome_arquivo = os.path.basename(arquivo_origemdata)
    caminho_arquivo_destino = os.path.join(pasta_data, nome_arquivo)

    print(f'Tentando salvar o arquivo em: {caminho_arquivo_destino}')

    if not os.path.exists(caminho_arquivo_destino):
        shutil.copy(arquivo_origemdata, caminho_arquivo_destino)
        print(f'Arquivo copiado para a pasta {data_formatada}.')
    else:
        print(f'O arquivo já existe na pasta {data_formatada}.')

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
