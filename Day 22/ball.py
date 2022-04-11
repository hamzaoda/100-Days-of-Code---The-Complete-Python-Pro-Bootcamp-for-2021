from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.body = self.createBody()
        self.x_move = 10
        self.y_move = 10
        
    def createBody(self):
        new_shape = Turtle(shape = 'circle')
        new_shape.speed('slow')
        new_shape.penup()
        new_shape.color('white')
        new_shape.goto(0, 0)
        return new_shape
    
    def move(self):
        new_y = self.body.ycor() + self.y_move
        new_x = self.body.xcor() + self.x_move
        self.body.goto(new_x, new_y)
        
    def bounce(self):
        self.y_move *= -1
        
        
    def bounceOnPaddle(self):
        self.x_move *= -1

        