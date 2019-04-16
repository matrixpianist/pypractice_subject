import pygame
import os
import sys
import time
from   pygame.locals import *

pygame.init()

#Colours here
RED      =  pygame.Color(150,   0,   0)
GREEN    =  pygame.Color(  0, 150,   0)
BLUE     =  pygame.Color(  0,   0, 150)
BLACK    =  pygame.Color(  0,   0,   0)
WHITE    =  pygame.Color(255, 255, 255)

FPS = pygame.time.Clock()

WIDTH  = 1024
HEIGHT = 768
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Penaldo v0.1')

#Set BACKGROUND to an instance of pygame.Surface, which will get its coordinates from the previous ones we assigned to the game's display
BACKGROUND = pygame.Surface((SCREEN.get_width(), SCREEN.get_height()))

SCREEN.blit(BACKGROUND, (0, 0))

key_press = pygame.key.get_pressed()

class Player():
    def __init__(self):


        #Try to load our sprite.
        #'r' makes it a raw string so it ignores escape sequences

        self.player = pygame.image.load(r"\..\..\resources\mario_sprite_by_killer828-d3iw0tz.png")
        self.p_rect = self.player.get_rect()

        #Spawn the player just in the middle of our screen
        self.p_rect.centerx = WIDTH / 2
        self.p_rect.centery  = HEIGHT / 2

    def move(self):
        if key_press[UP]:
            self.p_rect.y -= 5

        elif key_press[DOWN]:
            self.p_rect.y += 5

        elif key_press[LEFT]:
            self.p_rect.x -= 5

        elif key_press[RIGHT]:
            self.p_rect.x += 5

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
        #Some IDLE friendliness (prevents from hanging)
            pygame.quit()
            sys.exit()


    BACKGROUND.fill(GREEN)

    p1 = Player()

    # FOR THE GAME TO WORK you have to include this one inside main while-loop (no display update = no game)
    pygame.display.update()
FPS.tick(40)
