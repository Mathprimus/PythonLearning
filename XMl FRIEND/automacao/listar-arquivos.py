import os
import time


def listar_arquivos(diretorio):
    print(f"Listando arquivos no diretório: {diretorio}")
    try:
        for dirpath, dirnames, filenames in os.walk(diretorio):

            for arquivo in filenames:
                if arquivo.lower().endswith(".xml"):
                    caminho_completo = os.path.join(dirpath, arquivo)
                    print(f"Arquivo XML encontrado: {caminho_completo}")

            for subdir in dirnames:
                print(f"Subdiretório: {os.path.join(dirpath, subdir)}")

    except FileNotFoundError:
        print("Diretorio nao encontrado")
    except Exception as e:
        print(f"Erro ao listar arquivos: {e}")



def monitorar_diretorio(diretorio, intervalo=5):
    while True:
        listar_arquivos(diretorio)
        time.sleep(intervalo)

def colocar_diretorio():
    caminho = input(str('Coloque o caminho, por favor'))
    return os.path.normpath(caminho)


caminho_diretorio = colocar_diretorio()


monitorar_diretorio(caminho_diretorio)
