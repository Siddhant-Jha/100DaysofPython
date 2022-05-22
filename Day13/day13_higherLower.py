#DAY 13 Final Project: Minute Details left


#WAP to play the game of higer or lower
#A game where you have to guess than from the above mentioned celebrities have more followers
#If you are right the game will continue but if you are wrong, Program will stop and display your score
#When you are right B become A

#importing the choice function from random module, and game data
from random import choice
from day13_gameData import data


#Welcome prompt for the users
print("""

                                                                **************************
                                                                  WELCOME TO THE GAME OF
                                                                    HIGHER OR LOWER        
                                                                **************************

""")

#Function to pick a celebrity at random

def pickCeleb():
    return choice(data)


#Function to ask user for input
def userGuess():
    userGuess = input(f"""
                    You have to guess, Weather {celebA['name']} who is a {celebA['description']} and lives in {celebA['country']} 
                                                                                
                                                                                or

                    {celebB['name']} who is a {celebB['description']} and lives in {celebB['country']} has higer or lower number of followers

                    Type 'H' for Higer or 'L' for Lower\t""").lower()
    
    return userGuess


#Function to check the answer

def answerCheck(celebA, celebB, userGuess):
    celebAFollowers = celebA['follower_count']
    celebBFollowers = celebB['follower_count']

    if celebBFollowers > celebAFollowers and userGuess == 'h':
        return True
    elif celebBFollowers > celebAFollowers and userGuess == 'l':
        return False
    elif celebAFollowers > celebBFollowers and userGuess == 'h':
        return False
    elif celebAFollowers > celebBFollowers and userGuess == 'l':
        return True


celebA = pickCeleb()
celebB = pickCeleb()

totalScore = 0


answer = answerCheck(celebA=celebA, celebB=celebB, userGuess=userGuess())


while answer == True:
    if answer == True:
        print("You Win")
        totalScore += 1
        celebA = celebB
        celebB = pickCeleb()
        answer = answerCheck(celebA=celebA, celebB=celebB, userGuess=userGuess())
        
print("You Loose")
print(f"You final score is {totalScore}")
