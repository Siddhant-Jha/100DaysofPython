#WAP for users to order pizza
#Small Pizza = 100
#Medium Pizza = 200
#Large Pizza = 300
#Paneer for small pizza = 20    Paneer for medium and large pizza = 50
#Extra Cheese = 10


#Defining variables for calculations
paneerSmall = 20
paneerLarge = 50
cheese = 10
totalBill = 0

#Welcome promt for the user
print("Hey There, Welcome to The Python Pizza")


#Taking input from the user regrading his choice
choice = input("What size pizza would you like to have today, Type 'S' for Small, 'M' for Medium, and 'L' for Large\t")
paneer = input("Do you want Paneer on your Pizza. Type 'Y' for Yes and 'N' for No\t")
extraCheese = input("Would you like to have Extra cheese on Pizza. Type 'Y' for Yes and 'N' for No\t")

#The Conditional Part

if choice == 'S':           #If the user selectes a Small Pizza, This block will be executed
    totalBill += 100
    if paneer == 'Y':
        totalBill += paneerSmall
    if extraCheese == 'Y':
        totalBill += cheese
    print(f"Your total bill amount is {totalBill}")

elif choice == 'M':
    totalBill += 200
    if paneer == 'Y':
        totalBill += paneerLarge
    if extraCheese == 'Y':
        totalBill += cheese
    print(f"Your total bill amount is Rs. {totalBill}")

else:
    totalBill += 300
    if paneer == 'Y':
        totalBill += paneerLarge
    if cheese == 'Y':
        totalBill += 10
    print(f"Your total bill amount is {totalBill}")