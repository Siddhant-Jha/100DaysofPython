#WAP to calculate the maximum height from a give list of height's without using min or max function

#Welcome Prompt for the user
print("Hey There, Welcome to the Max Height calculator app, This app will find the maximum height from a list of height's without using max() function")

listOfHeights = input("Please enter the list of height's separated by spaces").split(" ")

maximumHeight = 0

for height in listOfHeights:
    if maximumHeight > float(height):
        maximumHeight = float(height)
        print(f"The maximum height is {maximumHeight}")
    else:
        print(f"The maximum lenght is {height}")
        #NOT YET COMPLETED
