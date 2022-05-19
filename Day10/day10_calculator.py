#DAY 10 Final Project

#WAP to create a calculator

#Defining functions for each individual operation

def addition (numberOne, numberTwo):
    return numberOne + numberTwo


def subtraction (numberOne, numberTwo):
    return numberOne - numberTwo


def multiplication (numberOne, numberTwo):
    return numberOne * numberTwo


def division (numberOne, numberTwo):
    return numberOne / numberTwo


#Adding all the functions inside a dictonary

calculation = {
    "+": addition,
    "-": subtraction,
    "*": multiplication,
    "/": division,
}

#Using recursion function

def freshCalculation():

    again = True

    numberOne = float(input("Please enter the first number:\t"))

    for operator in calculation:
        print(f"{operator}\n")

    while again == True:

        userChoice = input("Please enter the operation you want to perform:\t")

        numberTwo = float(input("Please enter the next number:\t"))

        calculationOperation = calculation[userChoice]

        answer = calculationOperation(numberOne,numberTwo)

        print(f" {numberOne} {userChoice} {numberTwo} = {answer}")

        continueOrNot = input("Do you want to continue the calculation with the available result or Start a new calculation or Exit the program\n Type 'C' for Continue \n Type 'N' for New Calculation \n Type 'E' to Exit\t").lower()

        if continueOrNot == 'c':
            numberOne = answer

        elif continueOrNot == 'n':
            freshCalculation()

        else:
            again = False

freshCalculation()
