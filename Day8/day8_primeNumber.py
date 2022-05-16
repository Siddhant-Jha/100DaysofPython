#WAP to check if a given number is a prime number or not
#Prime numbers are the numbers that are only divisible by 1 and itself and no other number's

#Welcome prompt for the users


print("Hey there, I will help you to check if a given number is a prime number or not")

def primeOrNot(number):
    isPrime = True
    for value in range(2,number):
        if number%value == 0:
            isPrime = False
    if isPrime == True:
        print(f"The number entered by you i.e. {number} is a Prime number")
    else:
        print(f"The number entered by you {number} is not a Prime number")
        


#Asking user to enter a value

number = int(input("Please enter a number to check if the given number is prime or not\t"))

#Calling the function with argument as number
primeOrNot(number=number)