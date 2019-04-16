import pygame
import random

BLACK = (0,0,0)
pygame.init()
screen = pygame.display.set_mode([800,600])
pygame.display.set_caption("Smiley Explosion")
mousedown = False
keep_going = True
clock = pygame.time.Clock()
pic = pygame.image.load("F:/pypractice/teach_your_kids_to_code/9-10/smiley.png")
colorkey = pic.get_at((0,0))
pic.set_colorkey(colorkey)
sprite_list = pygame.sprite.Group()

class Smiley(pygame.sprite.Sprite):

"""
--------------------------------------------------------------------------------------------------------
定义了class类之后，大家可以看到，该类中包含了固定的值以及在类当中定义的函数，
其中，函数也有嵌套运用了其它函数的情况，在函数和类当中定义的值，只能够在该桉树或者类当中应用
--------------------------------------------------------------------------------------------------------
"""

    pos = (0,0)
    xvel = 1
    yvel = 1
    scale = 100

    def __init__(self, pos, xvel, yvel):
        pygame.sprite.Sprite.__init__(self)
        self.image = pic
        self.scale = random.randrange(10,100)
        self.image = pygame.transform.scale(self.image, (self.scale,self.scale))
        self.rect = self.image.get_rect()
        self.pos = pos
        self.rect.x = pos[0] - self.scale/2
        self.rect.y = pos[1] - self.scale/2
        self.xvel = xvel
        self.yvel = yvel

    def update(self):
        self.rect.x += self.xvel
        self.rect.y += self.yvel
        if self.rect.x <= 0 or self.rect.x > screen.get_width() - self.scale:
            self.xvel = -self.xvel*(0.5)
        if self.rect.y <= 0 or self.rect.y >screen.get_height() - self.scale:
            self.yvel = -self.yvel*(0.5)

while keep_going:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            keep_going = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mousedown = True
        if event.type == pygame.MOUSEBUTTONUP:
            mousedown = False

    screen.fill(BLACK)
    sprite_list.update()
    sprite_list.draw(screen)
    clock.tick(60)
    pygame.display.update()
    if mousedown:
        speedx = random.randint(0,0)
        speedy = random.randint(-5,0)
        newSmiley = Smiley(pygame.mouse.get_pos(), speedx, speedy)
        sprite_list.add(newSmiley)

pygame.quit()
