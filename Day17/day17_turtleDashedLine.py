from turtle import Screen, Turtle

newTurtle = Turtle()
screen = Screen()


for _ in range(10):
    newTurtle.forward(10)
    newTurtle.penup()
    newTurtle.forward(10)
    newTurtle.pendown()
    newTurtle.forward(10)

screen.exitonclick()