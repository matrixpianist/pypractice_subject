# SpiralFamily.py
import turtle   # Set up turtle graphics
t = turtle.Pen()
turtle.bgcolor("gray")
colors = ["red","yellow","blue","green","orange","purple","white","brown","black","pink"]
family = []  # Set up an empty list for family names

# Ask for the first name
name = turtle.textinput("My family", "Enter a name, or just hit [ENTER] to end: ")
# Keep asking for names
while name != "":
    # Add their name to the family list
    family.append(name)
    # Ask for another name, or end
    name = turtle.textinput("My family", "Enter a name, or just hit [ENTER] to quit.")

# Draw a spiral of the names on the screen
for x in range(100):
    t.pencolor(colors[x%len(family)]) # Rotate through the colors
    t.penup()                         # Don't draw the regular spiral lines
    t.forward(x * 4)                  # Just move the turtle pen
    t.pendown()                       # Draw the next family numbers name
    t.write(family[x%len(family)], font = ("Arial", int((x + 4)/4),"bold"))
    t.left(360/len(family) + 2)       # Turn left for our spiral
