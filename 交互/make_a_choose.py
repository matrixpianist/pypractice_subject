from tkinter import *
import easygui

root = Tk()
root.title('编程语言大战 !')
v = IntVar()
photo = PhotoImage(file="F:/桌面壁纸/11.gif")    # 声明一下图片 .
def callback():
    easygui.msgbox('你这样让我很不爽',title='你说呢?')

group=LabelFrame(root,text='最好的编程语言是 ?')   # 基于root 制定一个框架 . 
group.pack(padx=50)

v.set(1)
Language = [('Python',1),
            ('ruby',2),
            ('C++',3),
            ('java',2)
        ]
for lang,num in Language:
    b = Radiobutton(group,text=lang,variable=v,value=num,indicatoron=False,padx=30,pady=3)
    l = Label(group,textvariable=v)  # 将内容添加到框架当中
    l.pack()
    b.pack(anchor=W,fill=X)

theButton=Button(root,text='就是这个了',command=callback)
theButton.pack(pady=20)
mainloop()
