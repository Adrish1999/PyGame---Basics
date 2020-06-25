import pygame
import sys
from pygame.locals import *

pygame.init()

#Set up the window
DISPLAYSURF = pygame.display.set_mode((400,300),0,32)
pygame.display.set_caption("Drawing")

#Set up the colors
BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)

#Draw on the surface object
DISPLAYSURF.fill(WHITE)
pygame.draw.polygon(DISPLAYSURF,GREEN,((25,75),(76,125),(250,375),(400,25),(60,540)))
pygame.draw.line(DISPLAYSURF,BLUE,(60,60),(120,60),4)
pygame.draw.line(DISPLAYSURF,BLUE,(120,60),(60,120))
pygame.draw.line(DISPLAYSURF,BLUE,(60,120),(120,120),4)
pygame.draw.circle(DISPLAYSURF,BLUE,(300,50),20,0)
pygame.draw.ellipse(DISPLAYSURF,RED,(300,200,40,80),1)
pygame.draw.rect(DISPLAYSURF,RED,(200,150,100,50))

pixObj = pygame.PixelArray(DISPLAYSURF)
pixObj[380][280] = BLACK
pixObj[382][282] = BLACK
pixObj[384][284] = BLACK
pixObj[386][286] = BLACK
pixObj[388][288] = BLACK
del pixObj

#Run the game loop
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
