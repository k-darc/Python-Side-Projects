import random

def selected_questions():
    selected_questions = random.sample(list(questions.keys*()), 3)
    return {question: questions} for question in selected_questions

def quizgame():
    selected_questions = questions()
    correct = 0
    total_questions = len(questions)