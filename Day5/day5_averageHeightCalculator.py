#WAP to calculate the average height of students with a given list of height

#Welcome prompt for the users

print("Hey There, Welcome to the aveage height calculator app, It will help you to calcualte the average height from a given list of parameters")

#Declaring a variable to store the sum of the heights
sumOfHeight = 0

#Taking input from the user
listOfHeights = input("Please enter the heights of the students seperated by spaces\t").split(" ")

#Calculating the number of elements of the list to remove the depenedency on the loop using a counter
numberOfStudents = len(listOfHeights)

#For loop start's here, Have used type casting into float as height's can be in decimal/floating point notation
for singleHeight in listOfHeights:
    sumOfHeight += float(singleHeight)

#Instead of creating another variable to store the value of average height, Using the direct calculation menthod under print statement
print(f"The average height of the class is {sumOfHeight / numberOfStudents}")