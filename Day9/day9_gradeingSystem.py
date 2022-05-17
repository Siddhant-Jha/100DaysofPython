#Write a program to convert a dictonary with students name and score into a dictonary of student name and grades

# <70 : Fail
# 71-80 : Acceptable
# 81-90 : Exceeding Expectaion
# 91-100 : Outstanding

#Predefined dictonary with student name and score

studentScore = {
    "Laalu": 81,
    "Bhallu": 78,
    "Chaalu": 99,
    "Taplu": 74,
    "Kachra": 62,
}

#Defining an empty dictonary to hold the values of grades
studentGrades = {}

#Looping through the score dictonary to calculate the Grades
for student in studentScore:
    if (studentScore[student] < 70):
        studentGrades[student] = "Fail"
    elif (studentScore[student] > 7 and studentScore[student] <= 80):
        studentGrades[student] = "Acceptable"
    elif (studentScore[student] > 80 and studentScore[student] <= 90):
        studentGrades[student] = "Exceeding Expectations"
    else:
        studentGrades[student] = "Outstanding"

print(studentGrades)