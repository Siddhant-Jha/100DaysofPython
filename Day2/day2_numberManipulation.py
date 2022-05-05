#In this section we will see, how we can manipulate numbers and calculations

print(8/3)          #The output will be 2.6666666 as the resultant of simple division is ALWAYS an float number

#We can also round off the number using a inbuilt python function named round()

print(round(8/3))   #The output will be 3 because it round function rounds off the number and 2.6666 can be rounded off to 3

#We can also use the round fucntion to round off the values to a specific decimal digit

print(round((8/3),2))   #The answer will be 2.67 as it rounds off the number upto two decimal points

#We can also use floor division method, but the catch is that it will just chop of the values after the decimal

print(8//3)         #The answer will be 2 rather than 2.666
                    #It basically converts the result into int similar to type casting method



#########################################################
#                                                       #
#                   F-String                            #
#                                                       #
#########################################################

#Fstring is a pretty amazing function/utility of python and it omits the step where we have to convert everything into string to print something

height= 1.6
weight= 70
BMI= weight/(height ** 2)

#There are two ways to print all the information on the console

#APPROACH 1: Use type conversion
print("Your Height is " + str(height) + " , Your weight is " + str(weight) + "So your BMI is: " + str(BMI))

#APPROACH 2: The AWESOME one, Using F-String
print(f"Your Height is {height}, Your weight is {weight}, So accordingly your BMI is: {BMI}")