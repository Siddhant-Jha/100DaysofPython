tempInC = {
    "Monday":30,
    "Tuesday":32,
    "Wednesday":40,
    "Thursday":39,
    "Friday":28,
    "Saturday":31,
    "Sunday":30,
}

tempInF = {day:(temp * 9/5)+32 for (day,temp) in tempInC.items()}

print(tempInF)