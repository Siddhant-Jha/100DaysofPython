from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__(self)
        self.level = 1
        self.hideturtle()
        self.penup()
        self.goto(-280,250)
        self.writeLevel()


    def writeLevel(self):
        self.write(f"Level : {self.level}", align="left", font=FONT)

    def increaseLevel(self):
        self.level += 1
        self.clear()
        self.writeLevel()

    def gameOver(self):
        self.goto(0,0)
        self.write("Game Over", align="center", font=FONT)