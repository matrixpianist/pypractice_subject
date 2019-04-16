import turtle
import random
import tkinter
from tkinter import *

t = turtle.Pen()

a = ['所以，您今日的早餐最好吃：']
b = ["您的午餐可以考虑吃："]
c = ["您的晚餐可以选择："]

breakfast=[]
lunch=[]
dinner=[]
colors = ["black", "purple", "orange", "pink", "gray", "blue", "green", "yellow"]
def youmake():

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
    print("所以，您今日份的早餐可以是：", random.choice(breakfast))
    print("如果您不介意的话，午餐可以吃：", random.choice(lunch))
    print("看你这么懒，晚餐干脆就吃：", random.choice(dinner))
    

root=Toplevel()
frame1 = Frame(root)
frame2 = Frame(root)


abc = PhotoImage(file = "F:\pypractice\momkitchen\kitchenbg1.gif")
theLabel = Label(root, text = "欢迎来到妈咪厨房！你只需要输入你会做的饭，\n从此再也不用为做什么饭而烦恼！你要加入我们吗？", justify = LEFT, image=abc, compound = TOP, font = ("楷体", 20),fg = "black")
theButton = Button(frame2, text = "我要参加！", command = youmake)
theLabel.pack()
theButton.pack()

frame2.pack(padx = 10, pady = 10)

mainloop()
