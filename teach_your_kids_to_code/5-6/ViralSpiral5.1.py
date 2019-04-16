# ViralSpiral.py
import turtle
t = turtle.Pen()
t.penup()
turtle.bgcolor("gray")
sides = int(turtle.numinput("Number of sides", "How many sides in your spiral of spirals (2 - 10)?",4,2,10))
colors = ["red","yellow","blue","green","purple","orange","salmon","black","white","pink"]
for m in range(100):
    t.forward(m*4)
    position = t.position() # Renember this corner of the spiral
    heading = t.heading()   # Remember the direction we were heading
    if m%2 == 0:
        for n in range(int(m/2)):
            t.pendown()
            t.pencolor(colors[n%sides])
            t.forward(2*n)
            t.right(360/sides - 2)
            t.penup()
        t.setx(position[0]) # Go back to the big spiral's x location
        t.sety(position[1]) # Go back to the big spiral's y location
        t.setheading(heading)# Point in the big spiral's heading
        t.left(360/sides + 2)# Aim at the next point on the big spiral
    
    if m%2 != 0:
        for n in range(int(m/2)):
            t.pendown()
            t.pencolor(colors[n%sides])
            t.circle(2*n)
            t.right(360/sides - 2)
            t.penup()
        t.setx(position[0]) # Go back to the big spiral's x location
        t.sety(position[1]) # Go back to the big spiral's y location
        t.setheading(heading)# Point in the big spiral's heading
        t.left(360/sides + 2)# Aim at the next point on the big spiral
