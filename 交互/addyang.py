from tkinter import *
root = Tk()
root.title('皇上翻牌子啦!')    # 添加 初识框的标题 . 
GIRLS = ['西施','貂蝉','王昭君']         #  列表内容 . 
v = []  # 用于存放变量
for girl in GIRLS:
    v.append(IntVar())  # 声明一个 变量并且加入 v
    b = Checkbutton(root,text=girl,variable=v[-1],padx=80,font=('楷体',22)) #记录下来 变量的变化
    l = Label(root,textvariable=v[-1]) # 将变量表示为文本并且加入初始旷 . 
    l.pack(anchor=N)
    b.pack(anchor=W)
b = Checkbutton(root,text='杨玉环',variable=v[1],padx=80,font=('楷体',22))
l = Label(root,textvariable=v[1])
l.pack(anchor=N)
b.pack(anchor=W)
mainloop()
