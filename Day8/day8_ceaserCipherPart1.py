#WAP to encode or decode a message using ceaser cipher method
#STEP1: Encoding the message

def encrypt(message, shift):
    finalMessage = ""
    for alphabet in message:
        position = alphabets.index(alphabet)
        newPosition = position+shift
        newLetter = alphabets[newPosition]
        finalMessage += newLetter
    print(finalMessage)



def decrypt(message, shift):
    pass


#Defining the set of alphabets
alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

#Welcome prompt for the users
print("Welcome to the Ceaser Cipher")

#Taking inputs from the user's

choice = input("Do you want to Encode a message or Decode a message.\n Type 'Encode' or 'Decode'\t").lower()

if choice == 'encode':

    message = input("Enter the message you want to encrypt\t").lower()
    shift = int(input("Enter the shift value for the encoding\t"))
    encrypt(message=message ,shift=shift)

elif choice == 'decode':

    message = input("Enter the message you want to decode\t").lower()
    shift = int(input("Entered the shift value to decode the message"))
    decrypt(message=message, shift=shift)

else:

    print("Invalid Choice")

#END of STEP 1