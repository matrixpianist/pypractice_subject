from tkinter import *
root = Tk()
root.title('做饭时间到啦!')    # 添加 初识框的标题 . 
GIRLS = list(input("please input what kind of cook you can make."))         #  列表内容 . 
v = []  # 用于存放变量
for girl in GIRLS:
    v.append(IntVar())
    print(IntVar())
    b = Checkbutton(root,text=girl,variable=v[-1],padx=80,font=('楷体',22))
    b.pack(anchor=S)      # 文本的位置 . (东西南北的首拼 (英文))
mainloop()
