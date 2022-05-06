#WAP to create a Love Calculator, Where you calculate concurrent occerance of letters 'T,R,U,E' and 'L,O,V,E' in given set of names
#Then You add those individual numbers and obtain a two digit number and that''s the love percentage

#Example
#       T = 1             L = 2
#       R = 2             O = 2
#       U = 1             V = 1
#       E = 4             E = 4
#       ________________________
#           8                 9         So, your answer is 89%

#Welcome Prompt for the user
print("Hey There, Welcome to the Love Calculator")

#Taking input from the user i.e. name of both the person's
firstPerson = input("Please enter your name:\t").lower()
secondPerson = input("Please enter the name you want to check your compatibility with:\t").lower()

#Calculating The Love Percentage

#For TRUE
#Finding respective values of TRUE in the name of first persone
t = firstPerson.count('t')
r = firstPerson.count('r')
u = firstPerson.count('u')
e = firstPerson.count('e')

#Finding values of character in the name of second person
secondT= secondPerson.count('t')
secondR = secondPerson.count('r')
secondU = secondPerson.count('u')
secondE = secondPerson.count('e')

#Adding up the occurance of the characters for the word TRUE
sumOfTrue= t+r+u+e+secondT+secondR+secondU+secondE

#For LOVE
#Finding the occurance of letters LOV in the name of first person, Not finding the value of E as it is already available
l = firstPerson.count('l')
o = firstPerson.count('o')
v = firstPerson.count('v')

#Finding the occurance of letters LOV in the name of second person
secondL = secondPerson.count('l')
secondO = secondPerson.count('o')
secondV = secondPerson.count('v')

#Adding up the occurance of the letters for the word LOVE
sumOfLove = l+o+v+e+secondL+secondO+secondV+secondE

#Love Percentage
lovePercentage = str(sumOfTrue) + str(sumOfLove)
intLovePercentage = int(lovePercentage)


#The Conditional Begins

if (intLovePercentage <= 10 or intLovePercentage >= 90):
    print(f"Your Love Score is {lovePercentage}, You go together like coke and mentos")
elif (intLovePercentage >= 40 and intLovePercentage <= 50):
    print(f"Your love Score is {lovePercentage}, You are alrigth together")
else:
    print(f"Your love Score is {lovePercentage}")