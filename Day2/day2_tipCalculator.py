#DAY 2: Final Project

#WAP to calculate tip over a bill amount and split it into all the peoples dining in


#Welcome promt for the suer
print("Hey, There we hope that you had a great time dining in, this app will calcualte the amount of bill adding in the tip that each one of you have to pay")


#Taking in the bill amount from the user and type converting it into float, as bill amount can be in decimal points
billAmount= float(input("Please enter the bill amount:\t"))


#Taking in the tip value from the user, for convience it has been converted into float rather than int
tip= float(input("Please enter the amount of tip your want to give:\t"))


#Asking the user for the number of person, and converting the value into integer as number of person can't be in decimal
person= int(input("Please enter the number of people dining in today:\t"))


#Printing out the result and calculating the value simulataneously, Using the round function to round off the value upto second decimal point
print(f"The amount to be paid per persone is {round(((billAmount+(billAmount*(tip/100)))/person),2)}")
