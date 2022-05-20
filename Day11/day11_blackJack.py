# WAP to play the game of Black Jack

#Importing choice function from random moudlue to draw out a random card
from random import choice


#Welcome Prompt for the user
print("""

############################################################
                WELCOME TO CASINO ROYALE
                 
                 LET'S PLAY BLACK JACK
############################################################


""")


def drawCards():

    """ A function to randomly draw a card from deck of cards stated below where
        each face card holds the value of 10 and the Ace holds the value of 11 or 1 depending upon the situation
        If the user's total is going above 21 and user hold's an ACE it's value will be calculated as 1 instead of 11
    """

    deckOfCards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
    drawnCard = choice(deckOfCards)
    return drawnCard


def calculateScore (listofCards):

    """A function to calculate the sum of cards 
        and it will return 0 if sum of card's is 21 and the list hold's only 2 cards i.e. "Black Jack"
        If the total of cards is above 21 and user holds an ACE with value 11, it will remove it from the list and append a value of 1 instead.
    """

    if sum(listofCards) == 21 and len(listofCards) == 2:
        return 0
    
    if sum(listofCards) > 21 and 11 in listofCards:
        listofCards.remove(11)
        listofCards.append(1)
    
    return sum(listofCards)


def comparingCards (sumOfComputersCard, sumOfUsersCard):

    """ The main running horse of the program, It compares the card's of user and computer and return the resultant value
        check's if either user's total score or computer's total score is 0 i.e. Black Jack and declare them as winner's
    """
    if sumOfComputersCard == sumOfUsersCard:
        print("It's a Draw")

    elif sumOfComputersCard == 0:
        print("Computer has a black jack Computer Wins\n")
    elif sumOfUsersCard == 0:
        print("User have a black jack, User Wins\n")

    elif sumOfUsersCard > 21:
        print("Sum of User's card is higher than 21 You Loose\n")
    elif sumOfComputersCard > 21:
        print("Sum of Computer's card is higer than 21 You Win\n")
    elif sumOfUsersCard > sumOfComputersCard:
        print("You Win\n")
    else:
        print("You Loose\n")


def playBlackJack():

    """ Wrapped entire program into a function to improve repeatability.
        It defines two empty lists to hold cards of user and computer
        and a flag to keep the program running

        using for loop card's are appended to their respective list

        User is shown his entire set of cards and one card from the list computer's card

        Then sum of the card's is calculated 
        
        and if either user have a total of < 21, he is asked if he/she want's to draw another card
        if user say's yes another card is drawn at random and again totaling is done

        If the computer's total of cards is less than 17, he is bound to draw cards untill it's total reaches above 17

        At last card comparision is done and result is displayed

        At the end user is shown the completed set of computer's card as well

    """

    listOfUserCards = []
    listOfComputerCards = []
    gameOver = False

    for i in range(2):
        listOfUserCards.append(drawCards())
        listOfComputerCards.append(drawCards())

    print(f"Your card's are {listOfUserCards} and your total is {calculateScore(listofCards=listOfUserCards)}\n")

    print(f"Computer's card is {listOfComputerCards[0]}\n")

    while gameOver == False:

        sumOfUsersCard = calculateScore(listOfUserCards)
        sumOfComputersCard = calculateScore(listOfComputerCards)

        if sumOfUsersCard == 0 or sumOfComputersCard == 0 or sumOfUsersCard > 21:
            gameOver = True

        else:
            drawAnotherCard = input("\nDo you want to draw another card?\n\nType 'Y' for Yes or 'N' for No\t").lower()

            if drawAnotherCard == "y":
                listOfUserCards.append(drawCards())
            else:
                gameOver = True

    while sumOfComputersCard != 0 and sumOfComputersCard < 17:
        listOfComputerCards.append(drawCards())
        sumOfComputersCard = calculateScore(listofCards=listOfComputerCards)

    comparingCards(sumOfUsersCard=sumOfUsersCard, sumOfComputersCard=sumOfComputersCard)

    print(f"Computer's cards were {listOfComputerCards} and total was {sumOfComputersCard}\n")

#User is asked if he want's to play again
#If yes, the playBlackJack function is called again

while(input("\nDo You want to play Black Jack\n\nType 'Y' for Yes and 'N' for No\t").lower() == 'y'):
    playBlackJack()