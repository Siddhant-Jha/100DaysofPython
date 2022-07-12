import pandas

data = pandas.read_csv("Squirrel_Data.csv")
graySquirrelsCount = len(data["Primary Fur Color"] == "Gray")
blackSquirrelsCount = len(data["Primary Fur Color"] == "Black")
redSquirrelsCount = len(data["Primary Fur Color"] == "Cinnamon")

squirrelDict = {
    "Fur Color": ["Gray", "Black", "Cinnamon"],
    "Count": [graySquirrelsCount, blackSquirrelsCount, redSquirrelsCount]
}

squirrelDataframe = pandas.DataFrame(squirrelDict)
squirrelDataframe.to_csv("squirrelCount.csv")