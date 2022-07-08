from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__(self)

        self = Turtle("circle")
        self.color("white")
        self.penup()
        self.xMove = 10
        self.yMove = 10
        self.ballMoveSpeed = 0.2

    def move(self):
        newX = self.xcor() + self.xMove
        newY = self.ycor() + self.yMove
        self.goto(newX,newY)

    def bounce(self):
        newY = self.ycor() - self.yMove

    def paddleBounce(self):
        newX = self.xcor - self.xMove
        self.ballMoveSpeed *= 0.9
    
    def backToSquareOne(self):
        self.ballMoveSpeed = 0.1
        self.goto(0,0)
        self.paddleBounce()