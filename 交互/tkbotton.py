import tkinter
import tkinter.messagebox
from tkinter import * 
top = tkinter.Tk()
 
def helloCallBack():
   tkinter.messagebox.showinfo( "Hello Python", "Hello Runoob")
 
B = tkinter.Button(top, text ="点我", command = helloCallBack)
 
B.pack()
top.mainloop()

