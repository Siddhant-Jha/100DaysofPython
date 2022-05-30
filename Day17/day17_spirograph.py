from turtle import Turtle, Screen
from random import randint
import turtle

newTurtle = Turtle()
screen = Screen()
turtle.colormode(255)
newTurtle.speed("fastest")

def randomColor():
    randomRed = randint(0,255)
    randomGreen = randint(0,255)
    randomBlue = randint(0,255)
    randomColor = (randomRed,randomGreen,randomBlue)
    return randomColor


def drawSpirograph(sizeOfGap):

    for step in range(int(360/sizeOfGap)):
        newTurtle.color(randomColor())

        newTurtle.circle(100)
        newTurtle.left(sizeOfGap)

drawSpirograph(2)
screen.exitonclick()