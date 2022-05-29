#WAP for creating a quiz game

#Importing the question data from data.py
from day16_questionModel import Questions
from day16_data import question_data
from day16_quizBrain import QuizBrain
from random import randint

questionBank = []

for questions in range(len(question_data)):
    question = question_data[questions]['text']
    answers = question_data[questions]['answer']
    newQuestion = Questions(question,answers)

    questionBank.append(newQuestion)

quizBrain = QuizBrain(questionBank)

while quizBrain.questionNumber < len(questionBank):
    quizBrain.nextQuestion()
