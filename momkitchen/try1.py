from tkinter import *
import tkinter
import random
# 导入tkinter模块的所有内容
root = Tk()
c = ['z','2','3','4','5','a','rq','fg','ts']
# 创建一个文本Label对象
textLabel = Label(root,   # 将内容绑定在  root 初始框上面
text="您所下载的影片含有未成年人限制内容，\n请满18岁后再点击观看！",random.choice(a),justify=LEFT, padx=10)    
  
imgLabel = Label(root, image=photo)  
imgLabel.pack(side=RIGHT) 

mainloop()
