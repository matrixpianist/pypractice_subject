import turtle
import random
import tkinter
from tkinter import *

t = turtle.Pen()

choose = ["请","等","待","十","秒","!"]

breakfast=[]
lunch=[]
dinner=[]
colors = ["black", "purple", "orange", "pink", "gray", "blue", "green", "yellow", "brown", "red"]
def youmake():
    root = Tk()
    name = turtle.textinput("您会做的早餐：", "Enter a food name")
    while len(breakfast) <= 9:
        name = turtle.textinput("请继续输入：", "Enter a food name")
        breakfast.append(name)

    name1 = turtle.textinput("您会做的午餐：","Enter a food name")
    while len(lunch) <= 9:
        name1 = turtle.textinput("请继续输入：","Enter a food name")
        lunch.append(name1)

    name2 = turtle.textinput("最后，您会做的晚餐：","Enter a food name")
    while len(dinner) <= 9:
        name2 = turtle.textinput("请继续输入：","Enter a food name")
        dinner.append(name2)
    turtle.bgcolor("white")
    for x in range(50):
        t.pencolor(colors[x%len(choose)])
        t.penup()
        t.forward(x*4)
        t.pendown()
        t.write(choose[x%len(choose)], font = ("Arial", int((x+20)/4), "bold"))
        t.left(360/len(choose) + 2)

    root = Toplevel()
    photo = PhotoImage(file = "F:\pypractice\momkitchen\goodfood.gif")
    theLabel = Label(root, text = "请看命令窗口，您今日的专属菜谱已经生成", justify = LEFT, image=photo, compound = CENTER, font=("黑体", 20), fg = "blue")
    theLabel.pack()
    mainloop()
    
    a = ("所以，您今日份的早餐可以是：", random.choice(breakfast),"\n")
    b = ("如果您不介意的话，午餐可以吃：", random.choice(lunch), "\n")
    c = ("看你这么懒，晚餐干脆就吃：", random.choice(dinner), "\n")
    d = a + b + c

    root = Tk()
    photo1 = PhotoImage(file = "F:\pypractice\momkitchen\smile.gif")
    textLabel = Label(root,
                      text = d,
                      justify = LEFT, image = photo1, compound = CENTER, font = ("黑体", 20), fg = "black"
                     )
    
    imgLabel = Label(root, image = photo1)
    imgLabel.pack(side = RIGHT)

    mainloop()

root=Toplevel()
frame1 = Frame(root)
frame2 = Frame(root)


abc = PhotoImage(file = "F:\pypractice\momkitchen\kitchenbg1.gif")
theLabel = Label(root, text = "欢迎来到妈咪厨房！你只需要输入你会做的饭，\n从此再也不用为每天吃什么饭而烦恼！你要加入我们吗？", justify = LEFT, image=abc, compound = TOP, font = ("楷体", 20),fg = "black")
theButton = Button(frame2, text = "我要参加！", command = youmake)
theLabel.pack()
theButton.pack()

frame2.pack(padx = 10, pady = 10)

mainloop()
