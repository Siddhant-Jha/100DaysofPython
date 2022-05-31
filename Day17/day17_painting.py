from turtle import Turtle, Screen
from random import choice, randint
import turtle
#import colorgram


#Defining a new class named newTurtle, setting it's shape as circle
newTurtle = Turtle()
newTurtle.shape('circle')

#Defining a new class named screen to catch the screen
screen = Screen()

#changing the color mode to use 255
turtle.colormode(255)

#Defining empty list to hold our color pallet
listOfColors = []

#For loop to extract 10 random color, create a tuple out of it and appending it to the listOfColors for further use
for _ in range(10):
    r = randint(0,255)
    g = randint(0,255)
    b = randint(0,255)

    color = (r,g,b)
    listOfColors.append(color)

#Was planning to use this method but found it useless and image was not good looking
#colorsOfPicture = colorgram.extract('image.jpg',9)

# for color in colorsOfPicture:
#     position = 0
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b

#     colors = (r,g,b)
#     listOfColors.append(colors)

#TODO 1: Remove gitignore file

#Setting the turtle speed to fastest and using penup() function to remove the lines that used to be there
newTurtle.speed('fastest')
newTurtle.penup()

#Setting the postion of the turtle to suitable parameters
newTurtle.setheading(216)
newTurtle.forward(315)
newTurtle.setheading(0)

#instead of using the commands in the loop created a function to make a dot and move forward and another function to change the position of the turtle again
def dotAndForward():
    newTurtle.dot(20,(choice(listOfColors)))
    newTurtle.forward(50)

def leftAndForward():
    newTurtle.left(90)
    newTurtle.forward(50)
    newTurtle.left(90)
    newTurtle.forward(500)
    newTurtle.left(180)

#Setting the required number of dots
totalDots = 100


for dot in range(1, totalDots):

    dotAndForward()

    if dot % 10 == 0:
        leftAndForward()


screen.exitonclick()