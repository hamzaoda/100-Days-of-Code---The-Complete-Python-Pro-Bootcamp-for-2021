# import colorgram
from turtle import *
import random
import turtle as t



the_screen = Screen()
the_screen.setup(width=500, height=400)
user_bet = the_screen.textinput(title="Make your bet", prompt= "which turtle do you think will win ?")

colors = ["red", "green", "yellow", "blue", "purple", "orange", "black"]
y_indecies = [100, 50, 0, -50, -100]
all_turtles = []


for i in range(5):
    timmy = t.Turtle(shape='turtle')
    timmy.penup()
    timmy.color(colors[i])
    timmy.goto(-230, y_indecies[i])
    all_turtles.append(timmy)
        
if user_bet :
    race_on = True

while race_on :
    for turtle in all_turtles:
        if turtle.xcor() > 230 :
            race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"you've Won !!! the {winning_color} is the winner")
            else:
                print(f"you've Lost !!! the {winning_color} is the winner")

        rand_dist = random.randint(1, 10)
        turtle.fd(rand_dist)
    

        


the_screen.exitonclick()






