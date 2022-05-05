#WAP to Calculate BMI of a person if the weight is given in KG and height in M
#       BMI = Weight/Height^2


#Welcome prompt for the user
print("Hey, There welcome to the Body Mass Calculator App")


#Prompting the user for entering the weight in KG and Height in metre
#As we all know that input function takes an input in the form of a string so we have to convert it into floating point number
#As the weight and height can be in decimal orientaion

weight= float(input("Please enter your weight in Kilograms KG: \t"))
height= float(input("Plese enter your height in metres: \t"))


#Calculating the BMI and printing it on the console 
#But to concatinate it with the answer promt we have to convert the values into string
print("Your Body Mass Index i.e. BMI is " + str(weight/(height**2)))