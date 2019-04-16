import turtle
import random
import tkinter
from tkinter import *
colors = ["black", "purple", "orange", "pink", "gray", "blue", "green", "yellow"]
t = turtle.Pen()
turtle.bgcolor("black")

a = ['所以，您今日的早餐最好吃：']
b = ["您的午餐可以考虑吃："]
c = ["您的晚餐可以选择："]
t.pencolor(colors)
t.pendown()
t.write(b, font=("Arial", 20, "bold"))
