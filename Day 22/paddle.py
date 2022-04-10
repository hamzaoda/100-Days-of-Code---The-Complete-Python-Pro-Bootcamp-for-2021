from turtle import Turtle

UP = 90
DOWN = 270

class Paddle(Turtle):
    def __init__(self, positions):
        super().__init__()
        self.body = self.createBody(positions)
        
    def createBody(self, positions):
        new_square = Turtle(shape = 'square')
        new_square.speed('fastest')
        new_square.penup()
        new_square.shapesize(stretch_len= 1, stretch_wid= 5)
        new_square.color('white')
        new_square.goto(positions)
        return new_square
        
    def moveDown(self):
        new_y = self.body.ycor() - 20
        self.body.goto(self.body.xcor(), new_y)   
        
    def moveUp(self):
        new_y = self.body.ycor() + 20
        self.body.goto(self.body.xcor(), new_y)   
            