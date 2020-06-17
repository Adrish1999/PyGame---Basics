import pygame
import sys
import os
from pygame.locals import *

red = [255,0,0]

#Initialize pygame
pygame.init()

#Set up window
DISPLAYSURF = pygame.display.set_mode((400,300))
pygame.display.set_caption('Slither.eat - The Snake Game')

#Set up drawing surface
screen = pygame.display.get_surface()
screen.fill(red)
pygame.display.set_caption('Snake')
pygame.display.flip()q

count = 0

while True:
    for event in pygame.event.get():
        print(event)
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
