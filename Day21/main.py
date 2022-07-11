import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
carManager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.goUp, "Up")

gameOn = True
while gameOn:
    time.sleep(0.1)
    screen.update()

    carManager.createCar()
    carManager.moveCars()

    #Collision Detection
    for car in carManager.allCars:
        if car.distance(player) < 20:
            gameOn = False
            scoreboard.gameOver()

    #Succesfull Crossing
    if player.isAtFinish:
        player.gotoStart()
        carManager.levelUp()
        scoreboard.increaseLevel()


screen.exitonclick()
