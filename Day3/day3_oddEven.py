#WAP to check if a number is even or odd (Pretty Simple one)

#Welcome promt for the users
print("Hey There, This app will help you find out if the number entered by you is either EVEN or ODD")

#Asking users for the number
userInput= input("Please enter a number and I will try to find out if the number is EVEN or ODD\t")


#Start of the conditional statement
if (float(userInput) % 2 == 0):             #Converting the user input to a float one as the input recieved from the user is taken as a string
    print(f"The number entered by you {userInput} is an EVEN number")
else:
    print(f"The number entered by you {userInput} is an ODD number")