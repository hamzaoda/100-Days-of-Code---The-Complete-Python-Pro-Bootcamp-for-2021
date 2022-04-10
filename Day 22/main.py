from turtle import Screen
from paddle import Paddle
from ball import Ball
import time


screen = Screen()
l_paddle = Paddle((350, 0))
r_paddle = Paddle((-350, 0))
ball = Ball()

screen.setup(height=600, width=800)
screen.bgcolor('black')
screen.title('The Pong Game')
screen.tracer(0)

screen.listen()
screen.onkey(l_paddle.moveDown, 'Down')
screen.onkey(l_paddle.moveUp, 'Up')
screen.onkey(r_paddle.moveUp, 'w')
screen.onkey(r_paddle.moveDown, 's')


game_is_on = True
while game_is_on: 
    time.sleep(0.09)
    screen.update()
    ball.move()

    




















screen.exitonclick()