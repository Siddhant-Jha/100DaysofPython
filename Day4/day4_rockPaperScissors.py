#Day 4: Final Project
#WAP to play a rock paper scissor game between computer and user

#IMporting randint function from random module
from random import randint

#Asking user for his choice

userChoice = int(input("What do you want to choose, Type 0 for Rock\n Type 1 for Paper\n Type 2 for Scissors\t"))

computerChoice = randint(0,2)

rockPaperScissor = ["Rock", "Paper", "Scissor"]

if userChoice == computerChoice+1:
    print(f"You chose {rockPaperScissor[userChoice]} and Computer chose {rockPaperScissor[computerChoice]}, YOU WIN !!")

elif userChoice == computerChoice:
    print(f"You chose {rockPaperScissor[userChoice]} and Computer chose {rockPaperScissor[computerChoice]}, DRAW !!")

elif userChoice == 2 and computerChoice == 0:
    print(f"You chose {rockPaperScissor[userChoice]} and computer chose {rockPaperScissor[computerChoice]}, YOU LOSE !!")

elif userChoice == 0 and computerChoice == 2:
    print(f"You chose {rockPaperScissor[userChoice]} and Computer chose {rockPaperScissor[computerChoice]}, YOU WIN !!")

else:
    print(f"You chose {rockPaperScissor[userChoice]} and computer chose {rockPaperScissor[computerChoice]}, YOU LOSE !!")
