#WAP to take input from the user and calculate the number of character in the string

#There can be two approaches to this problem

#APPROACH 1: Using a varibale to store the value; Long method
userInput= input("Hey, There please enter a string to calcualte number of characters\t")
length= len(userInput)
length= str(length)
print("Length of the entered string is\t"+length)

#APPROACH 2: Using a shorthand menthod; Short method
#This is a one liner approach and working of the method is as follows:
#STEP 1: Firstly the input function will come into play and asks the user for input.
#STEP 2: After user enters the string, the string is then passed to the len function, which calculates the number of characters
#STEP 3: The value obtained from len function is then converted into str value because an int value can't be concatinated to a string
#STEP 4: The resultant value obtained from str function is then passed to the final print function and it get's concatinated with the text
#STEP 5: Output is displayed on the console
print("Number of characters in the given string is\t" + str(len(input("Hey There Enter a String to calculate number of characters\t"))))