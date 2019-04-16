from tkinter import *
root = Tk()
# 设置 滚动条 控制
sb = Scrollbar(root)  #  在 root 初始旷 上面插入一 插入一个滚动条 . 
sb.pack(side=RIGHT,fill=Y)      #  设置滚动条的位置 . 

text = Text(root ,width=30,height=10,yscrollcommand=sb.set) # 这个意思是每行三十个字符  两行 .  将滚动条 绑定在text文本上面 .  下面  txt文本会插入内容 . 
text.pack()
text.insert(INSERT,"I Love \n")#　第一个表示插入的位置　第二个是内容　其中第一个必须有　，　INSERT　是光标所在位置
text.insert(END,"Fishc.com !\n")  # END 表示 在上一次输入结束的位置继续 . 
photo = PhotoImage(file="F:/桌面壁纸/11.gif") # 打包一个图片 . 
def show():
    text.image_create(END,image=photo) #   在text 中添加一个 图片 .
button1 = Button(text,text="顶我! ",command=show) # 第一个和第二个的 text 可是不一样的,
text.window_create(INSERT,window=button1)  # 除了 文字是 insert 其余的好像都是 window_create
text.pack(side=LEFT,fill=BOTH)
sb.config(command=text.yview)            #   滚动条绑定   text的内容 用于  拉动滑块 反转内容 . 
mainloop()
