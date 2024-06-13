import random

questions = {
    "Question 1 TEST...": {"correct": "cat", "options": ["cat", "bike", "bird", "bike"]},}

def select_questions():
    selected_questions = random.sample(list(questions.keys()), 1)
    return {question: questions[question] for question in selected_questions}

def quiz():
    selected_questions = select_questions()
    correct_answers = 0
    total_questions = len(selected_questions)

def main():
    print("QUIZ!")
    print("Answer the questions")
    print()
    quiz()

if __name__ == "__main__":
    main()