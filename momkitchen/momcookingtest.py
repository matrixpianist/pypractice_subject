# Just a cooking test software
import turtle
t = turtle.Pen()
cooking_list = []
cooking_name = turtle.textinput("My cooking menu", "Enter in there!")
while cooking_name != "":
    cooking_list.append(cooking_name)
    cooking_name = turtle.textinput("Enter what you can cook", "Enter in there!")
    for x in range(21):
        t.penup()
        t.forward(x+50-x)
        t.pendown()
        t.write(cooking_name[x%len(cooking_name)],font = ('Arial', int(40), "bold"))
        
