import pygame
from time import sleep
print('Programa que toca audio com python')
pygame.init()
pygame.mixer.music.load('music.mp3')
pygame.mixer.music.play()
pygame.event.wait()
sleep(60)