from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.penup()
        self.color('white')
        self.goto(0, 250)
        self.showScore()
        
    def showScore(self):
        current_score = "Score : " + str(self.score)
        self.write(arg = current_score, align ='center', font = ('Arial', 22, 'normal'))
        
        
    def increaseScore(self):
        self.clear()
        self.score += 1
        self.showScore()
        
    def gameOver(self):
        self.goto(0, 0)
        self.write(arg = "GAME OVER", align ='center', font = ('Arial', 25, 'normal'))
