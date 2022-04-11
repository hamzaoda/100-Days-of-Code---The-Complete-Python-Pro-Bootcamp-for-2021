from turtle import Turtle
import random

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.body = self.createBody()
        self.randomStart()
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1
        
    def createBody(self):
        new_shape = Turtle(shape = 'circle')
        new_shape.speed('fastest')
        new_shape.penup()
        new_shape.color('white')
        return new_shape
    
    def move(self):
        new_y = self.body.ycor() + self.y_move
        new_x = self.body.xcor() + self.x_move
        self.body.goto(new_x, new_y)
        
    def bounce(self):
        self.y_move *= -1
        
        
    def bounceOnPaddle(self):
        self.move_speed *=0.9
        self.x_move *= -1
        
    def changeDirection(self):
        self.move_speed = 0.1
        self.body.home()
        self.x_move *= -1
    
    def randomStart(self):
        number = random.randint(0, 1)
        if number == 0:
            self.randomRightAngle()
        else:
            self.randomLeftAngle()
    
    def randomRightAngle(self):
        self.body.right(random.randint(0, 180))
        
    def randomLeftAngle(self):
        self.body.left(random.randint(180, 360))

        