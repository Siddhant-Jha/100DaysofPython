from turtle import Screen, Turtle, goto, ycor
from paddle import Paddle
from ball import Ball

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("The Pong Game")
screen.tracer(0)

#Moving to Paddle Class
# paddle = Turtle()
# paddle.shape("square")
# paddle.shapesize(stretch_wid=5, stretch_len=1)
# paddle.color("white")
# paddle.penup()
# paddle.goto(350,0)

rPaddle = Paddle(350,0)
lPaddle = Paddle(-350,0)

#Moving to Paddle.py
# def goUp():
#     newY = ycor() + 20
#     paddle.goto(paddle.xcor(), newY)

# def goDown():
#     newY = ycor() - 20
#     paddle.goto(paddle.xcor(), newY)

ball = Ball()

screen.listen()
screen.onkey(rPaddle.goUp , "Up")
screen.onkey(rPaddle.goDown, "Down")
screen.onkey(lPaddle.goUp, "w")
screen.onkey(lPaddle.goDown, "s")


gameOn = True
while gameOn:
    screen.update()
    ball.move()

    #Collision Detection

    if ball.ycor() > 280 or ball.ycor < -280:
        ball.bounce()

    if ball.distance(rPaddle) < 50 and ball.xcor > 320 or ball.distance(lPaddle) < 50 and ball.xcor < -320:
        ball.paddleBounce()

    #Miss Detection

    if ball.xcor() > 380:
        ball.backToSquareOne()

    if ball.xcor < -380:
        ball.backToSquareOne()

screen.exitonclick()