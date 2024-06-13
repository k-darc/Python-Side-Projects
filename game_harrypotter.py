import random

def questions():
    questions = random.sample(list(questions.keys*()), 3)
    return {question: questions} for question in questions