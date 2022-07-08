from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__(self)
        self.color("white")
        self.penup()
        self.hideturtle()
        self.rScore = 0
        self.lScore = 0
        self.updateScoreboard()

    def lPoint(self):
        self.lScore + 1
    
    def rPoint(self):
        self.rScore + 1
        
    def updateScoreboard(self):
        self.clear()
        self.goto(-100,200)
        self.write(self.lScore, align="center", font=("Courier", 80, "normal"))
        self.goto(100,-200)
        self.write(self.rScore, align="center", font=("Courier", 80, "normal"))