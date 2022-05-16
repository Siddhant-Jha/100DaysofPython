#DAY 8 Final Project

#WAP to encode or decode a message using ceaser cipher method

def ceaserCipher(choice, message, shift):
    finalMessage = ""
    for character in message:
        if character in alphabets:
            position = alphabets.index(character)
            if choice == 'encode':
                newPosition = position+shift
            elif choice == 'decode':
                newPosition = position-shift
            newLetter = alphabets[newPosition]
            finalMessage += newLetter
        else:
            finalMessage += character
    if choice == 'encode':
        print(f"\t The encoded Text is {finalMessage}")
    else:
        print(f"\t The decoded Text is {finalMessage}")


#Defining the set of alphabets
alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

#Welcome prompt for the users
print("\t \t \t \t \t Welcome to the Ceaser Cipher\n")

#Taking inputs from the user's

continueOrNot = "y"

while continueOrNot == 'y':

    choice = input("\n Do you want to Encode a message or Decode a message.\n Type 'Encode' or 'Decode'\t").lower()

    if choice == 'encode':

        message = input("\n Enter the message you want to encrypt\t").lower()
        shift = int(input("\n Enter the shift value for the encoding\t"))
        ceaserCipher(choice=choice, message=message, shift=shift)
        continueOrNot = input("\n Do you want to continue using the program\n Type 'Y' for 'Yes' and 'N' for 'No' \t").lower()


    elif choice == 'decode':

        message = input("\n Enter the message you want to decode\t").lower()
        shift = int(input("\n Entered the shift value to decode the message\t"))
        ceaserCipher(choice=choice, message=message, shift=shift)
        continueOrNot = input("\n Do you want to continue using the program\n Type 'Y' for 'Yes' and 'N' for 'No' \t").lower()

    else:

        print("Invalid Choice")
        continueOrNot = input("\n Do you want to continue using the program\n Type 'Y' for 'Yes' and 'N' for 'No' \t").lower()
