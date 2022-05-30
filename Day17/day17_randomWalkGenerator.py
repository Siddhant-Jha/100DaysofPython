from turtle import Turtle, Screen
from random import choice, randint
import turtle

newTurtle =Turtle()
screen = Screen()
turtle.colormode(255)

def randomColor():
    randomRed = randint(0,255)
    randomGreen = randint(0,255)
    randomBlue = randint(0,255)
    randomColor = (randomRed,randomGreen,randomBlue)
    return randomColor


directions = ['left','forward','right','backward']

newTurtle.pensize(10)

for _ in range(45):
    newTurtle.color(randomColor())
    steps = randint(9,45)
    movement = choice(directions)
    
    if movement == 'left':
        newTurtle.left(steps)
        newTurtle.forward(steps)
    elif movement == 'forward':
        newTurtle.forward(steps)
    elif movement == 'right':
        newTurtle.right(steps)
        newTurtle.forward(steps)
    else:
        newTurtle.backward(steps)

screen.exitonclick()