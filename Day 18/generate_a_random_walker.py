from turtle import *
import random

timy_the_turtle = Turtle()
colors = ["red", "green", "yellow", "blue", "purple", "orange", "black"]




def randomLines():
    for i in range(1,50):
        timy_the_turtle.right(random.choice([0, 90, 180, -90]))
        timy_the_turtle.fd(30)
        timy_the_turtle.color(random.choice(colors))
        timy_the_turtle.pensize(10)
        timy_the_turtle.speed(10)
        
    




randomLines()












the_screen = Screen()
the_screen.exitonclick()







