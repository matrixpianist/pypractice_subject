import pygame
pygame.init()
screen = pygame.display.set_mode([800,600])
keep_going = True
pic = pygame.image.load("F:/pypractice/teach_your_kids_to_code/9-10/smiley.png")
colorkey = pic.get_at((0,0))
pic.set_colorkey(colorkey)
picx = 0
picy = 0
BLACK = (0,0,0)
timer = pygame.time.Clock()   # 控制帧
speedx = 4
speedy = 3

while keep_going:   # 游戏循环
    for event in pygame.event.get():   # 第一个事件（控制退出的事件）
        if event.type == pygame.QUIT:   # 如果事件变为退出，就退出游戏循环
            keep_going = False

    picx += speedx
    picy += speedy

    if picx <= 0 or picx + pic.get_width() >= 800:
        speedx = -speedx

    if picy <= 0 or picy + pic.get_width() >= 600:
        speedy = -speedy

    screen.fill(BLACK)
    screen.blit(pic, (picx,picy))
    pygame.display.update()
    timer.tick(60)

pygame.quit()
