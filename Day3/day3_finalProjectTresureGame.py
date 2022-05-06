#DAY 3: FINAL PROJECT
#WAP to create a treasure hunting game

#Welcome prompt for the user
print("Hey there, welcome to the treaure hunting game.\n This is a story oriented game where your decisions can lead you up to some amazing treasure")

#Let's Begin the game
leftOrRight = input("You find a diverging road, Left one looks like a newly buit one, while the right one is a little worne out. Which direction would you like to go, Type 'L' for Left and 'R' for Right\t").lower()

if leftOrRight == 'l':
    knockOrNot = input("The road leads to an old cottage, Do you want to Knock the door for help or keep moving toward the Jungle ahead. Type 'K' for Knock or 'N' for No Knock\t").lower()
    if knockOrNot == 'y':
        agreeOrNot = input("You knock the door, an elderly men comes out of the door and you find out that he is a Forest Officer, You tell him about your aspiration about finding the treasure\n. He tells you that you should go back to the diversion and choose the road on the right.\n But you find his tone somewhat conspicious, What would you like to do now.\n Agree with what he said and go back to pick the road on the right or keep moving in the direction of the forest.\n Type 'A' to agree or 'N' to Not Agree\t").lower()
        if agreeOrNot == 'a':
            swimOrNot = input("You go back and take the road suggested by Forest Officer and at the end of the road finds a lake, upon whose horizion you seen a beautiful island.\n What would you like to do.\n Type 'W' to wait for a boat or type 'S' to swim across the lake to the island\t").lower()
            if swimOrNot == 'w':
                print("You wait for a boat and after some time a ship arrives there and take's you to the island and you find the treasure")

            else:
                print("You decide to swim through the lake, but get caught up by a group of sharks and dies\n 'GAME OVER'")
        
        else:
            print("You don't agree with the suggestion of Forest Officer and moves toward the Jungle and get killed by a pack of Wolf's \n 'GAME OVER'")
    else:
        print("You Decide not to knock the door and keep moving toward the jungle and get yourself killed by a giant mutated ANACONDA \n 'GAME OVER'")

else:
    waitOrSwim = input("At the end of the road you find a lake and across the lake you can see the treasure island\n Now you have two choices either you can wait for a boat or a ship or swim through the lake to the island\n Type 'S' to Swim or 'W' to wait\t").lower()
    if waitOrSwim == 'w':
        print("You wait for a boat and it leads you to the island, hurry, You found the treasure")
    else:
        print("You decide to swim through the lake, but get caught in torpedo and get yourself killed \n 'GAME OVER' ")
