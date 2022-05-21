#WAP to play the game of number guessing


#importing randint function from random module
from random import randint


#Defining a global variable for gussed number
GUESSEDNUMBER = randint(1,100)


def numberComparision(userGuess):
    if userGuess == GUESSEDNUMBER:
        print("You guessed it right!!!\n")
        return True
        
    elif userGuess < GUESSEDNUMBER:
        print("TOO LOW\n")
        return False
        
    else:
        print("TOO HIGH\n")
        return False
        


def mainLogic(numberOfLives):

    while numberOfLives > 0:
        userGuess = int(input("\nGuess a number:\t"))

        if numberComparision(userGuess=userGuess) == False:
            numberOfLives -= 1
            print(f"\nYou have {numberOfLives} attempts left")
        
        else:
            print("""
                    ############################

                            GAME OVER

                           !! YOU WIN !!
                    
                    ############################
        
                """)
        
        
    print("""

        ###############################

                    GAME OVER

                !! YOU LOST !!

        ###############################
            
        """)



#Welcome prompt for the user

print("""

###############################################

    WELCOME TO THE NUMBER GUESSING GAME

###############################################


I AM THINKING OF A NUMBER BETWEEN 1 AND 100

""")


#Asking user for the difficulty level

difficultyLevel = input("\n\nChoose your difficulty level\nType 'E' for Easy or 'H' for hard\t").lower()

if difficultyLevel == 'e':
    mainLogic(10)

elif difficultyLevel == 'h':
    mainLogic(5)

else: 
    print("INVALID INPUT")