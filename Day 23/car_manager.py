from turtle import Turtle
import random

COLORS = ["red", "green", "yellow", "blue", "purple", "orange", "black"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.createBody()
        self.move_speed = STARTING_MOVE_DISTANCE
     
    def createBody(self):
        self.shape('square')
        self.speed('fastest')
        self.penup()
        self.color(random.choice(COLORS))
        self.goto(300, random.randint(-100, 100)) 
        self.seth(180)
        self.shapesize(stretch_len = 1.5 )  
        
    def move(self):
        self.fd(self.move_speed)
        
        