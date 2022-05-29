class QuizBrain:
    def __init__(self,questionList):
        self.questionNumber = 0
        self.questionList = questionList
        self.score = 0
        
    def nextQuestion(self):
        currentQuestion = self.questionList[self.questionNumber]
        self.questionNumber += 1
        self.userAnswer=input(f"\nQ{self.questionNumber}: {currentQuestion.text} (True/False)\t")
        self.userScore(self.userAnswer, currentQuestion.answer)

    def userScore(self, userAnswer, correctAnswer):
        if userAnswer.lower() == correctAnswer.lower():
            self.score += 1
            print("\nYou are right\n")
        else:
            print("\nYou are wrong\n")

        print(f"\nYour current score is {self.score}/{self.questionNumber}\n")
        