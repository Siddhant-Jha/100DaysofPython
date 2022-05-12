#WAP to calculate the sum of all even numbers between 1 to 100 including 100

#Welcome Prompt for the user

print("Hey There, This program will help you to calculate the sum of all even number's between 1 to 100 including 100")

#Defining a variable to hold the sum of all even numbers
sumOfEven = 0

for number in range(1,101):
    if number%2 == 0:
        sumOfEven += number
print(f"The sum of all even number's between 1 and 100 including hundered is: {sumOfEven}")