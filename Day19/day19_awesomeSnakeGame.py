#MY AWESOME SNAKE GAME
#🥲🥲🥲🥲🥲🥲
#🥲🥲🥲🥲🥲🥲
#🥲🥲🥲🥲🥲🥲
#🥲🥲🥲🥲🥲🥲
#🥲🥲🥲🥲🥲🥲
#🥲🥲🥲🥲🥲🥲
#🥲🥲🥲🥲🥲🥲
#🥲🥲🥲🥲🥲🥲
#🥲🥲🥲🥲🥲🥲
#🥲🥲🥲🥲🥲🥲
#🥲🥲🥲🥲🥲🥲
#🥲🥲🥲🥲🥲🥲
#🥲🥲🥲🥲🥲🥲
#🥲🥲🥲🥲🥲🥲
#🥲🥲🥲🥲🥲🥲
#🥲🥲🥲🥲🥲🥲
#🥲🥲🥲🥲🥲🥲
#🥲🥲🥲🥲🥲🥲
#🥲🥲🥲🥲🥲🥲
#🥲🥲🥲🥲🥲🥲
#🥲🥲🥲🥲🥲🥲
#🥲🥲🥲🥲🥲🥲
#🥲🥲🥲🥲🥲😕

from turtle import Turtle, Screen
from time import sleep
from day19_snakeClass import CreateSnake

#Setting Up the screen
screen = Screen()
screen.setup(width=500, height=500)
screen.bgcolor("black")
screen.title("My Awesome Snake Game")
screen.tracer(0)
screen.listen()


snake = CreateSnake()


screen.onkeypress(key='Up', fun=snake.up())
screen.onkeypress(key='Down', fun=snake.down())
screen.onkeypress(key='Left', fun=snake.left())
screen.onkeypress(key='Right', fun=snake.right())


#Creating a snake
snake.createSnake()

gameOnn = True

while gameOnn:
    screen.update()
    sleep(0.1)
    snake.moveSnake()


screen.exitonclick()
