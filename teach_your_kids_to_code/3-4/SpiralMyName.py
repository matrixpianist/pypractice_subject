# SpiralMyName.py - print a colorful spiral of the user's name

import turtle
t = turtle.Pen()
turtle.bgcolor("gray")
colors = ["salmon","black","green","blue","yellow","red"]

# Ask the user's name using turtle's textinput pop-up window
your_name = turtle.textinput("Enter your name", "What is your name?")

# Draw a spiral of the name on the screen, written 100 times
for x in range(100):
    
    t.pencolor(colors[x%6]) # Rotate through the six colors
    t.penup()               # Don't draw the regular spiral lines
    t.forward(x*3/6 + x)          # Just move the turtle on the screen
    t.write(your_name, font = ("Arial", int((x + 6) / 6), "bold"))
    t.left(61)              # Turn left, just as in our other spirals
    
