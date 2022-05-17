#WAP to maintain a travel log to demonstrate the concept of dictonaries inside lists and nesting



#Pre defined travel log

travelLog = [
    {"country": "India",
    "visits" :100,
    "cities" : ["New Delhi", "Haridwar", "Rishikesh", "Ujjain", "Kedarnath"]
    },
    {"country": "America",
    "visits" : 10,
    "cities" : ["New York", "LA", "Las Vegas", "Miami"]
    },
]


#Function to add travel logs

def addNewCountry(country,visits,cities):
    newDict = {}

    newDict["country"] = country    #Adding every argument as a single entity for dictonary
    newDict["visits"] = visits
    newDict["cities"] = cities
    
    travelLog.append(newDict)

    print(travelLog)

addNewCountry(country="aloo",visits="gobi",cities = ["Paappu", "Chappu"])