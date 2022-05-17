#DAY 9 Final Project

#WAP to host a Silent Auction to depict the use of dictonaries

#Fucntion to compare the values of bidding amount
def compareBid(biddingRecord):
    maximumBid = 0
    maxbidder = ""
    for bidder in biddingRecord:
        if maximumBid < biddingRecord[bidder]:
            maximumBid = biddingRecord[bidder]
            maxbidder = bidder
    
    print(f"Winner of the Auction is {maxbidder} with the maximum bid of {maximumBid}")


#Welcome prompt for the users

print("Hey There, This application will hold a silent auction for you")

#Declaring an empty dictonary
biddingRecord = {}
moreBidders = 'y'


#Initiating the while loop to enable the user to enter names of multiple users
while moreBidders == 'y':

    name = input("Please enter your name:\t")
    biddingAmount = float(input("Please enter the amount you want to bid for the item: \t"))

    biddingRecord[name] = biddingAmount

    moreBidders = input("Do we have any more bidders.\n Type 'Y' for Yes and 'N' for No: \t").lower()


#Calling the compare bid function with argument of biddingRecord
compareBid(biddingRecord=biddingRecord)
