#WAP to calculate BMI of a user and according to the resultant value tell them about their BMI Interpretation

#Welcome promt for the users
print("Hey There, This is an advanced version of BMI calculator, That also tells you about the clincical interpretation of your calculated BMI")

#Taking Inputs around weight and height of the users
weight= input("Please tell me yor weight in Kilograms\t")
height= input("Please help me out with your height in Meters\t")

#Calculating the BMI of the user, using BMI=weight/height^2
BMI= round(float(weight)/(float(height) ** 2),2)      #BMI will be rounded to 2 digits after decimal

#Specificing and categorising the user according to the BMI value obtained
if BMI > 35:
    print(f"Your BMI value is {BMI} and you fall in the category of clinically obese, Plese lookout for medical help")
elif BMI > 30:
    print(f"Your BMI value is {BMI} and you fall under the category of Obese, You need to have a control on your lifestyle")
elif BMI > 25:
    print(f"Your BMI value is {BMI} and you fall under the category of overweight, Take a look on your diet and get some excercise")
elif BMI > 18.5:
    print(f"Your BMI valueis {BMI} and you fall under the category of normal weight, You are doing great keep up the good work")
else:
    print(f"Your BMI value is {BMI} and you fall under the category of Under Weight, Plese look after yourself and your diet")