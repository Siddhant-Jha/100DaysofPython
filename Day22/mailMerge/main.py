PLACEHOLDER = "[name]"

with open ("Mail Merge Project Start/Input/Names/invited_names.txt") as fileTwo:
    names = fileTwo.readlines()
    

with open("Mail Merge Project Start/Input/Letters/starting_letter.txt") as file:
    content = file.read()
    for name in names:
        strippedName = name.strip()
        newLetter = content.replace(PLACEHOLDER, strippedName)
        with open(f"Mail Merge Project Start/Output/ReadyToSend/{strippedName}.txt", mode= "w") as finalFile:
            finalFile.write(newLetter)
    
    
    
