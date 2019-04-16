import pygame
pygame.init()
screen = pygame.display.set_mode([600,600])
keep_going = True
pic = pygame.image.load("F:/桌面壁纸/jet1.png")
colorkey = pic.get_at((0,0))
pic.set_colorkey(colorkey)
picx = 0
picy = 0
BLACK = (0,0,0)
timer = pygame.time.Clock()
speed = 5
while keep_going:   # Game loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            keep_going = False
    picx += speed
    picy += speed

    if picx <= 0 or picx + pic.get_width() >= 600:
        speed = -speed

    screen.fill(BLACK)   # 屏幕填充为黑色
    screen.blit(pic, (picx,picy))   # 显示图像（在while循环中）
    pygame.display.update()   # 画面刷新
    timer.tick(60)

pygame.quit()   # Exit
