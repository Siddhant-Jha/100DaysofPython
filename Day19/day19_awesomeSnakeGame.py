#MY AWESOME SNAKE GAME

from turtle import Turtle, Screen

#Setting Up the screen
screen = Screen()
screen.setup(width=500, height=500)
screen.bgcolor("black")
screen.title("My Awesome Snake Game")


#Setting up three turtles simultaneously

startingPosition = [(0,0),(-20,0),(-40,0)]

for postion in startingPosition:
    snakeSegment = Turtle('square')
    snakeSegment.color('white')
    snakeSegment.goto(postion)



# #Function to move the turtles
# def moveForward():
#     turtleOne.forward(50)
#     turtleTwo.forward(50)
#     turtleThree.forward(50)

# screen.onkey(key='W', fun=moveForward)


screen.exitonclick()