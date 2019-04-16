# SquareSpiral1.py - Draws a square spiral
import turtle
t = turtle.Pen()
t.pencolor('blue')
for x in range(10000):
    t.circle(x)
    t.left(90)
