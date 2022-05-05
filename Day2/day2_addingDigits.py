#WAP to take input from user to get a two digit number and print the sum of digits of that number


#Asking user to input a two digit number
#Whenever we take an input from user, intrincily the input is in the form of a string
userInput= input("Hey, There please enter a two digit number and I will calculate the sum of digits of that number:\t")

#This step involves multiple operations, all the steps are mentioned below

#STEP 1: Takes the userInput variable at index 0 and  1 i.e. first and second digits respectively and converts them into interger to add them up
#STEP 2: Adds those two values
#STEP 3: Converts the output value of sum into string, because concatinating an interger to a string is not valid
#STEP 4: Concatinates and Prints the vale along with the string

sumOfDigits= print("Sum of the digits of number entered by you is " + str(int(userInput[0])+int(userInput[1])))