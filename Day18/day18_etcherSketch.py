from turtle import Turtle, Screen

newTurtle = Turtle()
screen = Screen()
screen.listen()

def moveForward():
    newTurtle.forward(20)

def moveBackward():
    newTurtle.back(20)

def moveLeft():
    turtleHead = newTurtle.heading()
    newTurtle.left(turtleHead)

def moveRight():
    turtleHead = newTurtle.heading()
    newTurtle.right(turtleHead)

def clearScreen():
    screen.reset()

screen.onkey(key="w", fun=moveForward)
screen.onkey(key="s", fun=moveBackward)
screen.onkey(key="a", fun=moveLeft)
screen.onkey(key="d", fun=moveRight)
screen.onkey(key="c", fun=clearScreen)

screen.exitonclick()