#Hangman STEP 1: Choosing a word from list and taking user input

#Importing the choice function to choose a random word from the list
from random import choice

#IMporting List of Words as a module
from day7_hangmanListOfWords import listOfWords

#Stages according to lives left
stage = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']


#Choosing a word from the list at random
chosenWord = choice(listOfWords).lower()

#Displaying the blanks
display = []    #Defining an empty list called display
for word in chosenWord:
    display += "_"

endOfGame = False
lives = 6

while endOfGame == False:
#Asking user to guess a letter
    userInput = input("Guess an alphabet\t").lower()

    #FOR LOOP to check if the alphabet choosen by user exists in the random word
    for position in range(len(chosenWord)):
        if userInput == chosenWord[position]: #Checking if the user selected alphabet exisits in the randomly choosen word
            display[position] = userInput

    if userInput not in chosenWord:
        lives -= 1
        print(f"You choose the letter {userInput} which is not in the choosen word, You lost a life")
        print(stage[lives])
        
    print(f"{''.join(display)}")

    if ("_" not in display) and lives >= 0:
        endOfGame = True
        print("Hurray!!!! You WON")
    elif lives == 0:
        endOfGame = True
        print("You Lost")
