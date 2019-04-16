import turtle
t = turtle.Pen()
colors = ["red", 'yellow', 'blue', 'green' , 'orange', 'black']
turtle.bgcolor('gray')
sides = 6
for x in range(360):
    t.pencolor(colors[x%sides])
    t.forward(x*3/sides + x)
    t.right(360/sides + 1)
    t.width(x*sides/200)
