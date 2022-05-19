# WAP to play the game of Black Jack

from random import choice

#Welcome Prompt for the user
print("""

############################################################
                WELCOME TO CASINO ROYALE
                 
                 LET'S PLAY BLACK JACK
############################################################


""")

#Defining the deck of cards Where all the face card's value 10 and ACE may be valued as a 11 or a 1 depending upon the situation

deckOfCards = [11,2,3,4,5,6,7,8,9,10,10,10,10]

#Function to add another card to user's deck
def addAnotherCardForUser():
    listOfUserCards.append(choice(deckOfCards))

def addAnotherCardForComputer():
    listOfComputerCards.append(choice(deckOfCards))


#Providing user and computer with two cards each

listOfUserCards = []
listOfComputerCards = []
sumOfUsersCard = 0
sumOfComputersCard = 0

for card in range(2):
    listOfUserCards.append(choice(deckOfCards))
    listOfComputerCards.append(choice(deckOfCards))

for card in range(len(listOfUserCards)):
    sumOfUsersCard += listOfUserCards[card]

for card in range(len(listOfComputerCards)):
    sumOfComputersCard += listOfComputerCards[card]


if (11 in listOfUserCards) and (10 in listOfUserCards):
    print("User Win's")
elif (11 in listOfComputerCards) and (10 in listOfComputerCards):
    print("Computer Win's")
else:
    if sumOfUsersCard > 21:
        if 11 in listOfUserCards:
            indexofAce = listOfUserCards.index(11)
            listOfUserCards[indexofAce] = 1

            if sumOfUsersCard > 21:
                print("You Lost")
            else:
                drawAnotherCard = input("Do you want to draw another card?\n Type 'Y' for Yes and 'N' for No: \t").lower()

                if drawAnotherCard == 'y':
                    addAnotherCardForUser
                else:
                    if sumOfComputersCard < 17:
                        addAnotherCardForComputer
                    else:
                        if sumOfComputersCard > 21:
                            print("Computer's Total is above 21 so You Win")
                        else:
                            if sumOfUsersCard > sumOfComputersCard:
                                print("Your Total is greater than Computer's total, You Win")
                            elif sumOfUsersCard == sumOfComputersCard:
                                print("Your Total score is equal to computer's score it's a Draw")
                            else:
                                 print("Your total is smaller than computer's total, You Lose")
            
        else:
            print("You Lost")

    else:
        drawAnotherCard = input("Do you want to draw another card? \n Type 'Y' for Yes or 'N' for NO")
        if drawAnotherCard == 'y':
            addAnotherCardForUser
        
        else:
            pass

print(listOfUserCards)
print(sumOfUsersCard)

print(listOfComputerCards)
print(sumOfComputersCard)

