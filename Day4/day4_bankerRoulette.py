#WAP to creaker a Banker Roulette app that takes names of persons and randomly chooses the person who is going to pay the bill

#Importing the random moudule for using randint function
from random import randint

#Welcome prompt for the users
print("Hey there, welcome to the Banker Roulette app, I will randomly choose a person who is going to pay the bill today")

#Taking input from the user regarding names of diners
namesOfDiners = input("Please enter the names of the peoples who are dinning today. sepearate the names of the diners with a comma\t")

#Converting the string input recieved from the user into a list by spliting the input using split function with seprator i.e. ", <Space>"
namesOfDiners_list = namesOfDiners.split(", ")

#Taking in the length of the list to use it as a parameter while using randint function
numberOfDiners = len(namesOfDiners_list)

#Printing a random name using randint function with starting point as 0 and numberOfDiners-1 because it gives the exact number of elements in the list but there index will be one less than that
print(f"Today's bill will be paid by {namesOfDiners_list[randint(0,numberOfDiners-1)]}")