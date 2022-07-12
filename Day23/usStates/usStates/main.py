import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S States")
backgroundImage = "usStates/usStates/blank_states_img.gif"
screen.addshape(backgroundImage)

turtle.shape(backgroundImage)

data = pandas.read_csv("usStates/usStates/50_states.csv")
allStates = data.state.to_list()
correctGuesses = []



while len(correctGuesses) < 50:
    userAnswer = screen.textinput(title=f"Guess the States {len(correctGuesses)}", prompt="Enter the name of the state").title()
    
    if userAnswer == "Exit":
        missedStates = []
        for state in allStates:
            if state not in correctGuesses:
                missedStates.append(state)
        missedStatesCSV = pandas.DataFrame(missedStates)
        missedStatesCSV.to_csv(missedStates.csv)
        break

    if userAnswer in allStates:
        correctGuesses.append(userAnswer)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        stateLocation = data[data.state == userAnswer]
        t.goto(int(stateLocation.x), int(stateLocation.y))
        t.write(userAnswer)

