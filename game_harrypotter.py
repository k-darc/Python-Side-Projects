import random

def select_questions():
    selected_questions = random.sample(list(questions.keys()), 3)
    return {question: questions for question in selected_questions}

def quiz():
    selected_questions = select_questions()
    correct_answers = 0
    total_questions = len(selected_questions)