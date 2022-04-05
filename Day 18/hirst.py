# import colorgram
from turtle import *
import random
import turtle as t


timy = t.Turtle()
t.colormode(255)
# colors = colorgram.extract('hirst.jpg', 30)


# new_colors= []
# for color in colors:
#     rgb= (color.rgb.r, color.rgb.g, color.rgb.b)
#     new_colors.append(rgb)


colors = [(198, 12, 32), (250, 237, 17), (39, 77, 189), (38, 217, 67), (238, 228, 5), (229, 159, 46), (27, 39, 158), (215, 74, 12), (15, 154, 16), (199, 14, 10), (242, 247, 252), (244, 33, 165), (229, 17, 122), (73, 9, 31), (60, 14, 8), (224, 141, 211), (222, 160, 8), (10, 98, 61), (17, 18, 43), (47, 214, 232), (11, 227, 239), (79, 72, 215), (237, 155, 222), (73, 213, 169), (78, 234, 201), (50, 234, 244), (3, 66, 40)]



timy.speed(1000)
timy.hideturtle()
timy.penup()


def hirstPainting():
    x = -250
    y = -250
    timy.setpos(x, y)
    for hight in range(1, 10):
        for i in range(1,10):
            timy.fd(50)
            timy.dot(20, random.choice(colors))
        y +=50
        timy.setpos(x, y)
        


hirstPainting()

        
the_screen = Screen()
the_screen.exitonclick()







