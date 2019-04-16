#This is just a round
import turtle
t = turtle.Pen()
turtle.bgcolor('gray')
sides = 3
colors = ['red', 'yellow', 'blue', 'orange', 'green', 'purple']
for x in range(360):
    t.pencolor(colors[x%sides])
    t.forward(x*3/sides + x)
    t.right(360/sides + 1)
    t.width(x*sides/200)
