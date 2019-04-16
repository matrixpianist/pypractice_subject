import turtle
import random
t = turtle.Pen()
t.speed(0)
t.hideturtle()  # 隐藏了画笔
turtle.bgcolor("gray")
colors = ["red", "yellow", "blue", "white", "green", "orange", "pink", "salmon", "black"]

def draw_kaleido(x,y):
    t.pencolor(random.choice(colors))
    size = random.randint(10,40)
    draw_spiral(x,y, size)
    draw_spiral(-x,y, size)
    draw_spiral(-x,-y, size)
    draw_spiral(x,-y, size)

def draw_spiral(x,y, size):
    t.penup()
    t.setpos(x,y)
    t.pendown()
    for m in range(size):
        t.forward(m*2)
        t.left(92)
turtle.onscreenclick(draw_kaleido)
