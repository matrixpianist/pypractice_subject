breakfast=[]
lunch=[]
dinner=[]

def youmake():
    name = turtle.textinput("请输入你会做的早餐：", "Enter a food name")
    while len(breakfast) <= 9:
        name = turtle.textinput("请继续输入你会做的早餐：", "Enter a food name")
        breakfast.append(name)

    name1 = turtle.textinput("请输入你会做的午餐：","Enter a food name")
    while len(lunch) <= 9:
        name1 = turtle.textinput("请继续输入你会做的午餐：","Enter a food name")
        lunch.append(name1)

    name2 = turtle.textinput("最后一步，请输入你会做的晚餐：","Enter a food name")
    while len(dinner) <= 9:
        name2 = turtle.textinput("最后一步，请继续输入你会做的晚餐：","Enter a food name")
        dinner.append(name2)
        
    print("所以，您今日的早餐最好吃：", random.choice(breakfast))
    print("您的午餐可以考虑吃：", random.choice(lunch))
    print("您的晚餐可以选择：", random.choice(dinner))
