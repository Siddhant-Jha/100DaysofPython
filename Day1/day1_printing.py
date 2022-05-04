
#Printing a sting
print("Hello World! with double quotes")        #Print's a string " " are used to print the strings, they signifies that
                                                # It is not a code and you have to print it as it is, no calcualtion required

print('Hello World! with single quotes')        #Instead of using " " we can also make use of ' ' for stings


#Printing Hello World Multiple times in different lines but using a single command
print("Hello World!\nHello World! second time\nHello World third time")     #We use \n flag to indicate a newline character


#Printing nth character of a string made easy
#We can now easily print any character from a string using the method mentioned below
print("Hello Appi!"[6])                         #We can right the index we want to catch from the string and python will automatically print that for us


#Printing number but with equal gaps(tabs) inbetween
print("1\t2\t3\t4\t5")      #We make use of \t flag to denote a tab in the print function
print("6\t7\t8\t9\t10")


#Produces an error when we try to print a string without " "
"""print(Hello World)    # It will give a syntax error"""


#Using print function to calcuate values
print(2+2)             #Output --> 4 When no " " are used and any sort of arthimatic part is under print function
                       #Rather than printing as it is, it calculates the values first


#Using print function to print value of a variable
firstVariable=1                        #Defining a variable with name firstVariable with value 1
secondVariable=2                       #Defining second variable with value 2
print(firstVariable)                   #Print's value of firstVariable
print(secondVariable)                  #Print's value of secondVariable
print(firstVariable+secondVariable)    #Calculates the sum of firstVariable and secondVariable and then prints the value

#Printing multiple items in one go
print("Hello World! in one go", 2+2, firstVariable, secondVariable, firstVariable+secondVariable)


#String concatination
print("Hello" + " World!\n")              #Sting concatination means addition of two sting values


#String Multiplication
print("*\t"*5)                          #Sting multiplication is used to print a single stirng multiple times
print("*\t"*4)                          #Helps out to make patterns
print("*\t"*3)
print("*\t"*2)
print("*\n\n")

print("*\t"*1)
print("*\t"*2)
print("*\t"*3)
print("*\t"*4)
print("*\t"*5)