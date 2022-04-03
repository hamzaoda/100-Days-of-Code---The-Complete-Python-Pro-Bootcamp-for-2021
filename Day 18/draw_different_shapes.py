from turtle import *


timy_the_turtle = Turtle()



def drawSquare(angle, number):
    for i in range(1, number+1):
        timy_the_turtle.right(angle)
        timy_the_turtle.fd(100)
        
    

timy_the_turtle.shape('turtle')
timy_the_turtle.color('red')


for i in range(3,16):
    angle = 360 / i
    drawSquare(angle, i)













the_screen = Screen()
the_screen.exitonclick()







