import pygame
import random

pygame.init()
screen = pygame.display.set_mode([800,600])
pygame.display.set_caption("Click and drag to draw")
keep_going = True
radius = random.randint(10, 25)
a = random.randint(0,255)
b = random.randint(0,255)
c = random.randint(0,255)
COLOR = (a, b, c)   # COLOR在此处被定义为一个元组

mousedown = False

while keep_going:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            keep_going = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mousedown = True
        if event.type == pygame.MOUSEBUTTONUP:
            mousedown = False

    if mousedown:

        spot = pygame.mouse.get_pos()

        pygame.draw.circle(screen, COLOR, spot, radius)
    pygame.display.update()   # Update display

pygame.quit()
