from turtle import *


timy_the_turtle = Turtle()
the_screen = Screen()


def drawDashedLine():
    timy_the_turtle.fd(10)
    

timy_the_turtle.shape('turtle')
timy_the_turtle.color('red')


for i in range(0,21):
    if i % 2 == 0:
        timy_the_turtle.penup()
    else:
        timy_the_turtle.pendown()
    drawDashedLine()














the_screen.exitonclick()







