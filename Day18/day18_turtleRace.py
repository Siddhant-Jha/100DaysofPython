from turtle import Turtle, Screen
from random import randint

screen = Screen()
screen.setup(height=500, width=500)
raceOnn = False
userBet = screen.textinput(title="Make Your Bet", prompt="Who will win Red/Green/Blue")


turtleName = ['turtleOne', 'turtleTwo', 'turtleThree']
colors =['red','green','blue']
yPosition = [-50,0,50]


for turtleNumber in range(3):
    
    turtleName[turtleNumber] = Turtle(shape='turtle')
    turtleName[turtleNumber].color(colors[turtleNumber])

    turtleName[turtleNumber].penup()

    turtleName[turtleNumber].goto(x = -230, y = yPosition[turtleNumber])


if userBet:
    raceOnn = True

while raceOnn == True:
    
    for turtle in turtleName:

        if turtle.xcor() > 230:
            winningTurtle = turtle.pencolor()

            if winningTurtle == userBet:
                print("You won the bet")
            else:
                print(f"You lost the bet and the winning color is {winningTurtle}")
            
            raceOnn = False

        turtle.forward(randint(0,10))

    


screen.exitonclick()