import turtle
import random
t = turtle.Pen()
t.speed(0)
t.hideturtle()  # 隐藏了画笔
turtle.bgcolor("gray")
colors = ["red", "yellow", "blue", "white", "green", "orange", "pink", "salmon", "black"]

def draw_kaleido(x,y):
    draw_smiley(x,y)
    draw_smiley(-x,y)
    draw_smiley(-x,-y)
    draw_smiley(x,-y)

def draw_smiley(x,y):
    t.penup()
    t.setpos(x,y)
    t.pendown()
    # Head
    t.pencolor(random.choice(colors))
    t.fillcolor(random.choice(colors))
    t.begin_fill()
    t.circle(50)
    t.end_fill()
    t.penup()
    # Left eye

    t.setpos(x-15, y+60)
    t.pendown()
    t.fillcolor(random.choice(colors))
    t.begin_fill()
    t.circle(10)
    t.end_fill()
    t.penup()
    # Right eye

    t.setpos(x+15, y+60)
    t.pendown()
    t.begin_fill()
    t.circle(10)
    t.end_fill()
    t.penup()
    # Mouth

    t.setpos(x-25, y+40)
    t.pendown()
    t.pencolor(random.choice(colors))
    t.width(5)
    t.goto(x-10, y+20)
    t.goto(x+10, y+20)
    t.goto(x+25, y+40)
    t.width(1)

turtle.onscreenclick(draw_kaleido)
