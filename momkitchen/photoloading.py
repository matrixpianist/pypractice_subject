import tkinter
from tkinter import *
def youmake():
    pass
root=Tk()
frame1 = Frame(root)
frame2 = Frame(root)


photo = PhotoImage(file = "F:\pypractice\momkitchen\kitchenbg1.gif")
theLabel = Label(root, text = "欢迎来到妈咪厨房！你只需要输入你会做的饭，\n从此再也不用为做什么饭而烦恼！你要加入我们吗？", justify = LEFT, image=photo , compound = TOP, font = ("楷体", 20),fg = "black")
theButton = Button(frame2, text = "我要参加！", command = youmake)
theLabel.pack()
theButton.pack()

frame2.pack(padx = 10, pady = 10)

mainloop()
