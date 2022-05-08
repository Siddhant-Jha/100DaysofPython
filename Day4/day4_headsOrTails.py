#DAY4: Not completed
#WAP to simulate a coin toss incorporating the use of random module
#0 is a Head and 1 is a Tail

#Importing the random module
import random

#Welcome prompt for the user
print("Hey There, Welcome to the coin toss program")

headOrTail = random.randint(0,1)    #This will generate a random number between 0 and 1

if headOrTail == 0:
    print("Head's")
else:
    print("Tails")
