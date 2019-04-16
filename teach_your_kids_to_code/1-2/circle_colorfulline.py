import turtle
t = turtle.Pen()
colors = ["red", 'yellow', 'blue', 'green' , 'orange', 'black', 'purple', 'salmon']
turtle.bgcolor('gray')
sides = 8
for x in range(640):
    t.pencolor(colors[x%sides])
    t.circle(x*4/sides + x)
    t.right(640/sides +1)
    t.width(x*sides/200)
