import pygame

pygame.init()

mu1 = 'C:\\Users\\Matheus\\Documents\\musicas\\AC_DC - Ballbreaker.mp3'
mu2 = 'C:\\Users\\Matheus\\Documents\\musicas\\AC_DC - Dogs of War.mp3'
mu3 = 'C:\\Users\\Matheus\\Documents\\musicas\\AC_DC - Highway to Hell (Official Video).mp3'
lista = [mu1, mu2, mu3]

print("Escolha a música:")
for i, musica in enumerate(lista):
    print(f"{i + 1}. {musica}")

escolha = int(input("Digite o número da música desejada: "))

if 1 <= escolha <= len(lista):
    pygame.mixer.music.load(lista[escolha - 1])
    pygame.mixer.music.play()

while pygame.mixer.music.get_busy():
    pygame.time.Clock().tick(10)
else:
    print("Escolha inválida!")
