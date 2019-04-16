import turtle
from tkinter import *
enorde = turtle.textinput("Keybord window", 'Enter e or d to begin:')
if enorde == 'e':
    emessage = turtle.textinput("Keybord window", "Enter a message to encode: ")
    emessage = emessage.upper()
    long = len(emessage)
    eoutput = ""
    for letter in emessage:
        if letter.isupper():
            value = ord(letter) + long
            letter = chr(value)
            if not letter.isupper():
                value -= long*2
                letter = chr(value)
        eoutput += letter
        
    root = Toplevel()
    photo = PhotoImage(file = "F:/桌面壁纸/t11.gif")
    textLabel = Label(root, text = eoutput, justify = CENTER, image = photo, compound = CENTER, font = ("黑体", 40), fg = "white")
    textLabel.pack()

    mainloop()
          
else:
    dmessage = None
    print("Ok, it seems like you dont need any kind of code here, your code is:", dmessage)
