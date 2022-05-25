#WAP for coffee dispenser

#Importing coffeeMenu
import day14_coffeeMenu


#Function for asking user for his/her choice

def userChoice():
    print("""
    
                                    ##############################################
                                    #                                            #
                                    #               WELCOME TO                   #
                                    #                                            #
                                    #               CAFE MAHADEV                 #
                                    #                                            #
                                    ##############################################
    
    
    
    
    """)
    userWant = input("\nWelcome to Cafe Mahadev\nWhat would you like to have today\n1. Espresso for Rs. 150\n2. Latte for Rs. 250\n3. Cappuccino for Rs. 300: \t").lower()
    return userWant

#Function to generate a report
def generateReport():
    print(f"\n\nWater Left: {day14_coffeeMenu.resources['water']}\nMilk Left: {day14_coffeeMenu.resources['milk']}\nCoffee Left: {day14_coffeeMenu.resources['coffee']}\nTotal Money earned is {day14_coffeeMenu.totalMoney}\n\n")

#Function to make diffrent coffees
def makeEspresso():
    day14_coffeeMenu.resources['water'] -= 50
    day14_coffeeMenu.resources['coffee'] -= 18
    print("\nYour Espresso is ready ☕, Please Enjoy\n")

def makeLatte():
    day14_coffeeMenu.resources['water'] -= 200
    day14_coffeeMenu.resources['milk'] -= 150
    day14_coffeeMenu.resources['coffee'] -= 24
    print("\nYour Latte is ready ☕, Please Enjoy\n")

def makeCappuccino():
    day14_coffeeMenu.resources['water'] -= 250
    day14_coffeeMenu.resources['milk'] -= 100
    day14_coffeeMenu.resources['coffee'] -= 24
    print("\nYour Cappuccino is ready ☕, Please Enjoy\n")

#Function to check resources
def resourceChecker(userWant):
    if userWant == 'espresso':
        if day14_coffeeMenu.resources['water'] >= 50 and day14_coffeeMenu.resources['coffee'] >= 18:
            return True
        else:
            print("Sorry therer is not enough resources left\n")
            return False
    
    elif userWant == 'latte':
        if day14_coffeeMenu.resources['water'] >= 200 and day14_coffeeMenu.resources['coffee'] >= 24 and day14_coffeeMenu.resources['milk'] >= 150:
            return True
        else:
            print("Sorry therer is not enough resources left\n")
            return False
    
    elif userWant == 'cappuccino':
        if day14_coffeeMenu.resources['water'] >= 250 and day14_coffeeMenu.resources['coffee'] >= 24 and day14_coffeeMenu.resources['milk'] >= 100:
            return True
        else:
            print("Sorry therer is not enough resources left\n")
            return False

#TODO 1: Even though the resources are not enough, coffe is still being made, STOP IT

#Function to calculate coins

def coinCalculator(userWant):
    totalAmount = 0

    oneCoin = int(input("\nPlease enter number of coins with denomination Rs. 1\t"))
    twoCoin = int(input("Please enter number of coins with denomination Rs. 2\t"))
    fiveCoin = int(input("Please enter number of coins with denomination Rs. 5\t"))
    tenCoin = int(input("Please enter number of coins with denomination Rs. 10\t"))
    twentyCoin = int(input("Please enter number of coins with denomination Rs. 20\t"))


    totalAmount = oneCoin + (twoCoin*2) + (fiveCoin*5) + (tenCoin*10) + (twentyCoin*20)

    if userWant == 'espresso':
        if totalAmount < 150:
            print("\nThere is not enough money\n")
        else:
            print(f"\nYou have deposited {totalAmount} and you will receive a change of Rs.{totalAmount-150}\n")
            day14_coffeeMenu.totalMoney += 150
            return True

    elif userWant == 'latte':
        if totalAmount < 250:
            print("\nThere is not enough money")
        else:
            print(f"\nYou have deposited {totalAmount} and you will receive a change of Rs.{totalAmount-250}\n")
            day14_coffeeMenu.totalMoney += 250
            return True
    
    elif userWant == 'cappuccino':
        if totalAmount < 300:
            print("\nThere is not enough money\n")
        else:
            print(f"\nYou have deposited {totalAmount} and you will receive a change of Rs.{totalAmount-300}\n")
            day14_coffeeMenu.totalMoney += 300
            return True

turnOff = False

while turnOff != True:
    userWant = userChoice()


    if userWant == 'turnoff':
        turnOff = True
    
    if userWant == 'report':
        generateReport()
    
    else:
        if coinCalculator(userWant=userWant) == True and resourceChecker(userWant=userWant) == True:
            if userWant == 'espresso':
                makeEspresso()
            
            if userWant == 'latte':
                makeLatte()
            
            if userWant == 'cappuccino':
                makeCappuccino()
