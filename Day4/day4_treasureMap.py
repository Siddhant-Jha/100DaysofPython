#WAP to make a treasure map of sort
#The program will mark a spot with an 'X'. The code will accept two digit number as input where the first digit will be a column and second digit will the row

#       1       2       3
#  1  [⬜      ⬜     ⬜]
#  2  [⬜      ⬜     ⬜]
#  3  [⬜      ⬜     ⬜]

#Input 23 i.e. Coulmn 2 and Row 3

#Creating three rows with 3 blocks each

row1 = ["⬜", "⬜", "⬜"]
row2 = ["⬜", "⬜", "⬜"]
row3 = ["⬜", "⬜", "⬜"]

#fullMap is the key to success in this program, We will use the fullMap to edit the final output
fullMap= [row1, row2, row3]

#Printing the map before replacing the square's with user inputs
print(f"{row1}\n{row2}\n{row3}")

#Takeing input from the user i.e. A two digit number that will be later processed to harness valuable information
treasurePosition = input("Where do you want to put the treasure, enter a two digit number where first digit will denote column and second digit will be treated as row. \n Row <= 3 and Coulmn <= 3\t")

#Converting the user input into row's and coulmn's and typecasting them into integer as the output recieved from user will be in string and we need interger to proceed further
userRow = int(treasurePosition[1])  #Converting the value at first index i.e. Second digit into row number
userCoulmn = int(treasurePosition[0])   #Covnverting the Zero index into coulmn i.e. the second digit

fullMap[userRow-1][userCoulmn-1] = " X" #Now we use those values to replace the relative position of the row and coulmn index's, Using -1 because the value entered by the user will not be starting from 0

print(f"{row1}\n{row2}\n{row3}")    #Printing the map after replacing the block with an 'X'