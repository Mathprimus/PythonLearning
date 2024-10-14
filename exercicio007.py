import pygame

pygame.init()

musica = 'C:\\Users\\Matheus\\Documents\\musicas\\AC_DC - Ballbreaker.mp3'
pygame.mixer.music.load(musica)
pygame.mixer.music.play()
input()
pygame.event.wait()
