# WAP to play the game of Black Jack

from random import choice

#Welcome Prompt for the user
print("""

############################################################
                WELCOME TO CASINO ROYALE
                 
                 LET'S PLAY BLACK JACK
############################################################


""")


def drawCards():
    deckOfCards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
    drawnCard = choice(deckOfCards)
    return drawnCard


def calculateScore (listofCards):

    if sum(listofCards) == 21 and len(listofCards) == 21:
        return 0
    
    if sum(listofCards) > 21 and 11 in listofCards:
        listofCards.remove(11)
        listofCards.append(1)
    
    return sum(listofCards)


def comparingCards (sumOfComputersCard, sumOfUsersCard):
    if sumOfComputersCard == sumOfUsersCard:
        print("It's a Draw")
    elif sumOfComputersCard == 0:
        print("Computer has a black jack Computer Wins")
    elif sumOfUsersCard == 0:
        print("User have a black jack, User Wins")
    elif sumOfUsersCard > 21:
        print("Sum of User's card is higher than 21 You Loose")
    elif sumOfComputersCard > 21:
        print("Sum of Computer's card is higer than 21 You Win")
    elif sumOfUsersCard > sumOfComputersCard:
        print("You Win")
    else:
        print("You Loose")


def playBlackJack():

    listOfUserCards = []
    listOfComputerCards = []
    gameOver = False

    for i in range(2):
        listOfUserCards.append(drawCards)
        listOfComputerCards.append(drawCards)


    while gameOver == False:

        sumOfUsersCard = calculateScore(listofCards=listOfUserCards)
        sumOfComputersCard = calculateScore(listofCards=listOfComputerCards)


        if sumOfUsersCard == 0 or sumOfComputersCard == 0 or sumOfUsersCard > 21:
            gameOver = True

        else:
            drawAnotherCard = input("Do you want to draw and card?\n Type 'Y' for Yes or 'N' for No").lower()

            if drawAnotherCard == "y":
                listOfUserCards.append(drawCards)
            else:
                gameOver = True


    while sumOfComputersCard != 0 and sumOfComputersCard < 17:
        listOfComputerCards.append(drawCards)
        sumOfComputersCard = calculateScore(listofCards=listOfComputerCards)


    print(comparingCards(sumOfUsersCard=sumOfUsersCard, sumOfComputersCard=sumOfComputersCard))

while(input("Do You want to play Black Jack\nType 'Y' for Yes and 'N' for No").lower() == 'y'):
    playBlackJack()