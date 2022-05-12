#The popular Fizz Buzz Program

#Welcome prompt for the users

print("Hey There, this program will display all the number's b/w 1 to 100\n When the number is divisible by 3 it will print Fizz\n When the number is divisible by 5 it will print Buzz\n If the number is divisible by both 3 and 5, It will print FizzBuzz")

for number in range(1,101):
    if number%3 == 0 and number%5 == 0:
        print("FizzBuzz")
    elif number%5 == 0:
        print("Buzz")
    elif number%3 == 0:
        print("Fizz")
    else:
        print(number)