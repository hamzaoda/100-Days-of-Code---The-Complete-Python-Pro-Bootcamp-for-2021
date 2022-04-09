from turtle import Turtle

MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake :
    def __init__(self):
        self.squares = []
        for i in range(3):
            new_square = Turtle(shape = 'square')
            new_square.penup()
            new_square.color('white')
            new_square.goto(-20 * i,0)
            self.squares.append(new_square)
        self.head = self.squares[0]
    
    def move(self):
        for number in range(len(self.squares) - 1, 0 , -1):
            new_x = self.squares[number - 1].xcor()
            new_y = self.squares[number - 1].ycor()
            self.squares[number].goto(new_x, new_y)
        self.head.fd(MOVE_DISTANCE)
    
    
    def goRight(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
    
    def goLeft(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
    
        
    def goUp(self):
        if self.head.heading() != DOWN :
            self.head.setheading(UP)
    
    def goDown(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)   
    
    def add_new_segment(self):
            new_square = Turtle(shape = 'square')
            new_square.penup()
            new_square.color('white')
            new_square.goto(self.squares[-1].position())
            self.squares.append(new_square)