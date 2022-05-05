#WAP to calculate your time left on this earth if you are fortunate enough to live 90 years

#Welcome Prompt for the user

print("Hey There, this app will tell your how much time is left for you on this earth, if by God's grace, your were to live a life of 90 years")

#Asking the user for his name and current age, Using the split function to capture the input and split it to use distinctively
name,age= input("Please let me know your name and your current age respectivly and I will tell you how much time is left for you ").split()

#It's better to calcualte the time left beforehand rather than calculating it again and again, but first we have to convert the age into a integer
timeLeft= 90-int(age)

#Using F-String to ease out the procedure of printing and performing the calculations simulatneously
print(f"Hey {name}, Your time left on earth in years {timeLeft}, in months {timeLeft*12}, in weeks {timeLeft*52}, in days {timeLeft*365}")