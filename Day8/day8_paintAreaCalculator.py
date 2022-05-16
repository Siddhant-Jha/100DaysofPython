#WAP to calculate the number of paint can required to paint a particular surface area using functions
#1 Paint can cover's 5 Square Meter of surface area

#Number of can's = (Wall Height * Wall Width)/Paint can coverage i.e. 5
#Also round up the value

#Welcome prompt for the user
from math import ceil       #importong ceil function from the math module for rounding up the required paint can to a upper value

print("Hey, There I will help you to calculate the number of paint can's required to paint a particular wall")

def paintCanCalculator (heightofWall, widthofWall):
    numberOfPaintCan = (heightofWall*widthofWall)/5
    print(f"The number of paint can required to paint a wall of height {heightofWall} and width {widthofWall} is {ceil(numberOfPaintCan)}")

#Asking user's for the height and width of the wall
heightofWall = float(input("Please enter the height of the wall\t"))
widthofWall = float(input("Please enter the width of the wall to be painted\t"))

paintCanCalculator(heightofWall=heightofWall,widthofWall=widthofWall)