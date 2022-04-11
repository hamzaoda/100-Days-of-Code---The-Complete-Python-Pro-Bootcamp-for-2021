from turtle import Turtle

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.color('white')
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.updateScoreBoard()
        
    def updateScoreBoard(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.l_score, align = 'center', font=('Courier-Bold', 60, 'bold'))
        self.goto(100, 200)
        self.write(self.r_score, align = 'center', font=('Courier-Bold', 60, 'bold'))    
        
    def increaseScoreForLeft(self):
        self.l_score +=1
        self.updateScoreBoard()
        
    def increaseScoreForRight(self):
        self.r_score +=1
        self.updateScoreBoard()