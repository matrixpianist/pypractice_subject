import random
import turtle
t = turtle.Pen()
t.speed(0)
turtle.bgcolor("gray")
colors = ["red", "yellow", "blue", "green", "orange", "purple", "white", "black", "salmon"]
for n in range(50):
    # Generate spirals of random sizes/colors at random locations on the screen
    t.pencolor(random.choice(colors))
    size = random.randint(10, 40)
    # Generate a random (x,y) location on the screen
    x = random.randrange(0, turtle.window_width()//2)
    y = random.randrange(0, turtle.window_height()//2)
    # First spiral
    t.penup()
    t.setpos(x,y)
    t.pendown()
    for m in range(size):
        t.forward(m*2)
        t.left(91)
    # Second spiral
    t.penup()
    t.setpos(-x, y)
    t.pendown()
    for m in range(size):
        t.forward(m*2)
        t.left(91)
    # Third spiral
    t.penup()
    t.setpos(-x, -y)
    t.pendown()
    for m in range(size):
        t.forward(m*2)
        t.left(91)
    # Fourth spiral
    t.penup()
    t.setpos(x,-y)
    t.pendown()
    for m in range(size):
        t.forward(m*2)
        t.left(91)
