import turtle
import random
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
    print("Output message: ", eoutput)
          
else:
    dmessage = None
    print("Ok, it seems like you dont need any kind of code here, your code is:", dmessage)
