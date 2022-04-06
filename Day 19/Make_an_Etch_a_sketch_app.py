# import colorgram
from turtle import *
import random
import turtle as t


timy = t.Turtle()


def moveForward():
    timy.fd(20)


def moveBackward():
    timy.back(20)

def turnRight():
    timy.right(20)
    

def turnLeft():
    timy.left(20)
    

t.listen()
t.onkey(key = "w", fun = moveForward)
t.onkey(key = "a", fun = turnLeft)
t.onkey(key = "d", fun = turnRight)
t.onkey(key = "s", fun = moveBackward)
t.onkey(key = "c", fun = timy.reset)

        
the_screen = Screen()
the_screen.exitonclick()







