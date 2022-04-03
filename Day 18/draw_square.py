from turtle import *


timy_the_turtle = Turtle()
the_screen = Screen()


def drawSquare():
    timy_the_turtle.fd(50)
    timy_the_turtle.right(90)
    

timy_the_turtle.shape('turtle')
timy_the_turtle.color('red')


for i in range(0,4):
    drawSquare()














the_screen.exitonclick()







