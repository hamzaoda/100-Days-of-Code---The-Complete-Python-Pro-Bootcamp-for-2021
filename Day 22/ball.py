from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.body = self.createBody()
        
    def createBody(self):
        new_shape = Turtle(shape = 'circle')
        new_shape.speed('slow')
        new_shape.penup()
        new_shape.color('white')
        new_shape.goto(0, 0)
        return new_shape
    
    def move(self):
        new_y = self.body.ycor() + 10
        new_x = self.body.xcor() + 10
        self.body.goto(new_x, new_y)