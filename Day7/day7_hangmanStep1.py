#Hangman STEP 1: Choosing a word from list and taking user input

#Importing the choice function to choose a random word from the list
from random import choice

#Defining a list of words through which one random word will be choosen
listOfWords = ["Hello", "Bye", "Blue", "Green", "Black", "Batman"]

#Choosing a word from the list at random
chosenWord = choice(listOfWords).lower()

#Asking user to guess a letter
userInput = input("Guess an alphabet\t").lower()

#FOR LOOP to check if the alphabet choosen by user exists in the random word
for letter in chosenWord:
    if userInput == letter: #Checking if the user selected alphabet exisits in the randomly choosen word
        print("Right")
    else:
        print("Wrong")


#FIRST PART OF THE PROBLEM COMPLETED