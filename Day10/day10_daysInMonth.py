#WAP to print the number of day's in a given month after checking if the year is a leap year or not

#Function to check if the given year is a leap year or not

def leapOrNot(year):
    if year%4 == 0:
        if year%100 != 0:
            return True
        elif year%400 == 0:
            return True
        else:
            return False
    else:
        return False


#Defining function to return the days in a month

def daysInMonth(year, month):
    days = [31,28,31,30,31,30,31,31,30,31,30,31]
    if leapOrNot(year=year) and month == 2:
        return 29
    else:
        return days[month-1]

#Asking user for the inputs

year = int(input("Please enter the year, you want to check the day's in month: \t"))
month = int(input("Enter the number of month you want to check the days of: \t"))

#Checking validity of input's provided

if year <= 0 or month <= 0 or month > 12:
    print("Invalid Input")
else:
    print(f"Number of day's in the month of {month} in year {year} is {daysInMonth(year=year, month=month)}")