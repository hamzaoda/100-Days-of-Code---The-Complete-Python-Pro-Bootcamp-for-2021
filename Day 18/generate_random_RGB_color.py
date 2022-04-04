from turtle import *
import random
import turtle as t

timy_the_turtle = t.Turtle()
t.colormode(255)
# colors = ["red", "green", "yellow", "blue", "purple", "orange", "black"]

def random_colors():
    r = random.randint(0 ,255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    colors = (r, g, b)
    return colors

def randomLines():
    for i in range(1,1000):
        timy_the_turtle.right(random.choice([0, 90, 180, -90]))
        timy_the_turtle.fd(20)
        timy_the_turtle.color(random_colors())
        timy_the_turtle.pensize(10)
        timy_the_turtle.speed(10)
        
    




randomLines()












the_screen = Screen()
the_screen.exitonclick()







