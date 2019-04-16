import turtle
import random
t = turtle.Pen()
t.speed(0)
turtle.bgcolor("gray")
colors = ["red", "white", "blue", "yellow", "orange", "pink", "black", "salmon", "green"]
def spiral(x,y):
    t.pencolor(random.choice(colors))
    size = random.randint(10,40)
    t.penup()
    t.setpos(x,y)
    t.pendown()
    for m in range(size):
        t.forward(m*2)
        t.left(91)
turtle.onscreenclick(spiral)
