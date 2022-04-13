from turtle import Turtle

STARTING_POSTION = (0, -280)
MOVE_DISTANCE = 10
Finish_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.speed('fastest')
        self.penup()
        self.goto(STARTING_POSTION)
        self.seth(90)
        
    def move(self):
        self.fd(MOVE_DISTANCE)