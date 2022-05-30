from turtle import Turtle, Screen, color
from random import choice

newTurtle = Turtle()
screen = Screen()

colors = ['red', 'blue','green', 'yellow', 'pink', 'purple']

for side in range(3,11):
    
    for _ in range(side):
        newTurtle.forward(50)
        newTurtle.right(360/side)
        newTurtle.forward(50)

    newTurtle.color(choice(colors))

screen.exitonclick()