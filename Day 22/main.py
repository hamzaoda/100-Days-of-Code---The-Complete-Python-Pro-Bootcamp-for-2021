from turtle import Screen
from paddle import Paddle
from ball import Ball
import time


screen = Screen()
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()

screen.setup(height=600, width=800)
screen.bgcolor('black')
screen.title('The Pong Game')
screen.tracer(0)

screen.listen()
screen.onkey(r_paddle.moveDown, 'Down')
screen.onkey(r_paddle.moveUp, 'Up')
screen.onkey(l_paddle.moveUp, 'w')
screen.onkey(l_paddle.moveDown, 's')


game_is_on = True
while game_is_on: 
    time.sleep(0.1)
    screen.update()
    ball.move()
    
    if ball.body.ycor() > 290 or ball.body.ycor() < -290:
        ball.bounce()
    
    if ball.body.distance(r_paddle.body) < 50 and ball.body.xcor() > 320 or ball.body.xcor() < -320 and ball.body.distance(l_paddle.body) < 50:
        ball.bounceOnPaddle()
        
    if ball.body.xcor() > 380 :
        ball.changeDirection()
    
    if ball.body.xcor() < -380:
        ball.changeDirection()    

    




















screen.exitonclick()