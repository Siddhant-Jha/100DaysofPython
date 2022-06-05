import imp
from turtle import Turtle

STARTING_POSITION = [(0,0),(-20,0),(-40,0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class CreateSnake:
    
    def __init__(self):
        self.segments = []
        self.createSnake()
        self.head = self.segments[0]
        self.moveSnake()
        self.up()
        self.down()
        self.left()
        self.right()

    
    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
        
        
    #Creating Snake
    def createSnake(self):
        for postion in STARTING_POSITION:
            snakeSegment = Turtle('square')
            snakeSegment.color('white')
            snakeSegment.penup()
            self.segments.append(snakeSegment)
            snakeSegment.goto(postion)

    def moveSnake(self):
        for segmentNumber in range((len(self.segments)-1),0,-1):
            xCorOfPreviousSegment = self.segments[segmentNumber-1].xcor()
            yCorOfPreviousSegment = self.segments[segmentNumber-1].ycor()
            self.segments[segmentNumber].goto(x=xCorOfPreviousSegment,y=yCorOfPreviousSegment)

        self.head.forward(MOVE_DISTANCE)
