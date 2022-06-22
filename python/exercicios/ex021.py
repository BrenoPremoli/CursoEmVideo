import playsound
playsound.playsound('hino.mp3')
# --------------------------------------------------------------
import pygame
pygame.init()
pygame.mixer.music.load('hino.mp3')
pygame.mixer.music.play()
pygame.event.wait()

