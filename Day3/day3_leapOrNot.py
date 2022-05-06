#WAP to find out if a given year is a leap year or not

#The logic is that the year number must be divisble by 4
#And, NOT Clearly divisible by 100
#EXCEPT, if the year is clearly divisible by 400 as well

#Welcome prompt for the user
print("Hey there, Welcome to the app LEAP or NOT, This app will tell you if the year entered by you is leap or not")

#Gettign input from the user
year= int(input("Please enter a year, that you want to check:\t"))

#The MAGIC BEGINS

if year%4 == 0:
    if year%100 != 0:
        print(f"The year entered by you {year} is a LEAP year")
    elif year%400 == 0:
        print(f"The year entered by you {year} is a LEAP year")
    else:
        print(f"The year entered by you {year} is NOT a leap year")
else:
    print(f"The year entered by you {year} is NOT a leap year")