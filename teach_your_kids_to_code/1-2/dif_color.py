import turtle
t = turtle.Pen()
colors = ["red", 'yellow', 'salmon', 'green']
turtle.bgcolor('gray')
for x in range(1000):
    t.pencolor(colors[x%4])
    t.forward(x)
    t.right(45)
