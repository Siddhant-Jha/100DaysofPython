#WAP to generate a random password using the paranmeter's shared by the user

#Importing the random module
from random import choice, shuffle

#Welcome prompt for the user
print("Hey, There this program will help you generate random passwords to keep your account's secured")

#Defining the list of letter's, symbol's and number's
letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
symbols = ["#", "$", "%", "&", "'", "(", ")", "*", "+", ",", "-", ".", "/"]
numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]

#Asking user's for the Input's
numberOfLetters = int(input("How many letter's do you want in your password\t"))
numberOfSymbols = int(input("How many Symbol's do you want in your password\t"))
numberOfNumbers = int(input("How many Number's do you want in your password\t"))

#Defining two variables one that will hold the password element's as a list and other for storing the final password i.e. in String form
password = []
finalPassword =""


#For loop for working out with letter's
for letter in range(1,numberOfLetters+1):
    password.append(choice(letters))


#For loop for working out with symbol's
for symbol in range(1,numberOfSymbols+1):
    password.append(choice(symbols))


#For loop for working out with number's
for number in range(1,numberOfNumbers+1):
    password.append(choice(numbers))


#Shuffle function is a inbuilt function of random module and it shuffle's the element's of a list
shuffle(password)

#For loop for converting list into string for printing the final password
for character in password:
    finalPassword += character


#Printing out the final password
print(finalPassword)