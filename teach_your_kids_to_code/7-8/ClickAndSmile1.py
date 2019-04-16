import turtle
import random
t = turtle.Pen()
t.speed(0)
turtle.bgcolor("gray")
colors = ["red", "white", "blue", "yellow", "orange", "pink", "black", "salmon", "green"]
def draw_smiley(x,y):
    t.penup()
    t.setpos(x,y)
    t.pendown()
    # Head
    t.pencolor("yellow")
    t.fillcolor("yellow")
    t.begin_fill()
    t.circle(50)
    t.end_fill()
    # Left eye
    t.setpos(x-15, y+60)
    t.fillcolor("blue")
    t.begin_fill()
    t.circle(10)
    t.end_fill()
    # Right eye
    t.setpos(x+15, y+60)
    t.begin_fill()
    t.circle(10)
    t.end_fill()
    # Mouth
    t.setpos(x-25, y+40)
    t.pencolor("black")
    t.width(5)
    t.goto(x-10, y+20)
    t.goto(x+10, y+20)
    t.goto(x+25, y+40)
    t.width(1)

def draw_smiley1(x,y):
    draw_smiley.penup()
    draw_smiley.setpos(x,y)
    draw_smiley.pendown()
    # Head
    draw_smiley.begin_fill()
    draw_smiley.circle(50)
    draw_smiley.end_fill()
    # Left eye
    draw_smiley.setpos(x-15, y+60)
    draw_smiley.begin_fill()
    draw_smiley.circle(10)
    draw_smiley.end_fill()
    # Right eye
    draw_smiley.setpos(x+15, y+60)
    draw_smiley.begin_fill()
    draw_smiley.circle(10)
    draw_smiley.end_fill()
    # Mouth
    t.setpos(x-25, y+40)

    draw_smiley.goto(x-10, y+20)
    draw_smiley.goto(x+10, y+20)
    draw_smiley.goto(x+25, y+40)
    draw_smiley.width(1)
turtle.onscreenclick(draw_smiley1)
