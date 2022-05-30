#WAP to create a square using Turtle Module

from turtle import Turtle,Screen

#Initalising a Turtle
kaalu = Turtle()

kaalu.shape("circle")

kaalu.color("orange")


for movement in range (3):
    kaalu.forward(100)
    kaalu.left(90)

kaalu.forward(100)



screen = Screen()

screen.exitonclick()