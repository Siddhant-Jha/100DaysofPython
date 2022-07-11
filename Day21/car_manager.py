from turtle import Turtle
from random import choice, randint

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        super().__init__(self)
        self.carSpeed = STARTING_MOVE_DISTANCE
        self.allCars = []

    def createCar(self):
        randomChance = randint(1,6)
        if randomChance == 1:
            newCar = Turtle("square")
            newCar.shapesize(stretch_wid=1, stretch_len=2)
            newCar.penup()
            newCar.color(choice(COLORS))
            newY = randint(-250, 250)
            newCar.goto(300, newY)
            self.allCars.append(newCar)

    def moveCars(self):
        for car in self.allCars:
            car.backward(self.carSpeed)

    def levelUp(self):
        self.carSpeed += MOVE_INCREMENT
