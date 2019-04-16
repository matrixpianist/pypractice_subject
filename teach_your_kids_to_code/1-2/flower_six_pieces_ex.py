import turtle
t = turtle.Pen()
turtle.bgcolor('gray')
sides = 3
colors = ['red', 'yellow', 'blue', 'green', 'black', 'purple']
for x in range(360):
    t.pencolor(colors[x%sides])
    t.circle(x * 3/sides + x)
    t.left(360/sides + 1)
    t.width(x * sides/200)
