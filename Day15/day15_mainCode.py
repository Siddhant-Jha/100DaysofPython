#WAP to make a coffee machine using concepts of OOP

#Importing the required modules

from day15_menu import Menu, MenuItem
from day15_coffeeMaker import CoffeeMaker
from day15_moneyMachine import MoneyMachine


#Assigning the classes
myCoffeMaker = CoffeeMaker()
myMoneyMachine = MoneyMachine()
myMenu = Menu()

isMachineOn = True


while isMachineOn == True:
    options = myMenu.get_items()
    userChoice = input(f"\nWhat would you like to have today? {options}:\t")

    if userChoice == "turnoff":
        isMachineOn = False
    
    elif userChoice == "report":
        myCoffeMaker.report()
        myMoneyMachine.report()
    
    else:
        drink = myMenu.find_drink(userChoice)
        
        if myCoffeMaker.is_resource_sufficient(drink) and myMoneyMachine.make_payment(drink.cost):
            myCoffeMaker.make_coffee(drink)