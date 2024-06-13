import random

def main():
    print("QUIZ!")
    print("Answer the questions")
    print()
    quiz()

questions = {
    "What is the name of the potion that grants the drinker luck for a period of time?": {"correct": "Liquid Luck (Felix Felicis)", "options": ["Liquid Luck (Felix Felicis)", "Polyjuice Potion", "Veritaserum", "Amortentia"]},
    "What is the name of the spell that unlocks doors?": {"correct": "Alohomora", "options": ["Alohomora", "Accio", "Expelliarmus", "Expecto Patronum"]},
    "What is the name of the creature that guards the entrance to Gryffindor Tower?": {"correct": "The Fat Lady", "options": ["The Fat Lady", "The Grey Lady", "Nearly Headless Nick", "The Bloody Baron"]},
    "What is the name of the wizarding newspaper?": {"correct": "The Daily Prophet", "options": ["The Daily Prophet", "The Quibbler", "Witch Weekly", "The Daily Bugle"]},
    "What is the name of the ghost who haunts the Ravenclaw common room?": {"correct": "The Grey Lady", "options": ["The Grey Lady", "Nearly Headless Nick", "Moaning Myrtle", "The Bloody Baron"]},
    "What is the name of the magical village where Harry's parents were killed?": {"correct": "Godric's Hollow", "options": ["Godric's Hollow", "Hogsmeade", "Diagon Alley", "Ottery St. Catchpole"]},
    "What is the name of Hermione's cat?": {"correct": "Crookshanks", "options": ["Crookshanks", "Mrs. Norris", "Arnold", "Trevor"]},
    "What is the name of the sport played on broomsticks in the wizarding world?": {"correct": "Quidditch", "options": ["Quidditch", "Broomstick Racing", "Broomstick Polo", "Broomstick Football"]},
    "What is the name of the magical device used to store and review memories?": {"correct": "Pensieve", "options": ["Pensieve", "Time-Turner", "Deluminator", "Resurrection Stone"]},
    "What is the name of the curse that kills with a flash of green light?": {"correct": "Avada Kedavra", "options": ["Avada Kedavra", "Cruciatus Curse", "Imperius Curse", "Stupefy"]},
    "What is the name of Voldermort's snake?": {"correct": "Nagini", "options": ["Nagini", "Buckbeak", "Aragog", "Fang"]},
    "Who is the Potions Master at Hogwarts during Harry's time there?": {"correct": "Severus Snape", "options": ["Severus Snape", "Horace Slughorn", "Pomona Sprout", "Filius Flitwick"]},
    "What is the name of the organization founded by Albus Dumbledore to fight Voldemort?": {"correct": "The Order of the Phoenix", "options": ["The Order of the Phoenix", "The Death Eaters", "Dumbledore's Army", "The Ministry of Magic"]},
    "What is the name of the enchanted object that can reveal hidden messages?": {"correct": "The Marauder's Map", "options": ["The Marauder's Map", "The Pensieve", "The Remembrall", "The Sneakoscope"]},
    "What is the name of the device used to travel back in time?": {"correct": "Time-Turner", "options": ["Time-Turner", "Portkey", "Apparition", "Floo Powder"]},
    "What is the name of the object used to contain a fragment of the owners souls?": {"correct": "Horcrux", "options": ["Horcrux", "Portkey", "Pensieve", "Deluminator"]},
    "What is the name of the bank that goblins run in the wizarding world?": {"correct": "Gringotts", "options": ["Gringotts", "Ironbelly Bank", "Goblin Bank", "Green Godbank"]},
    "What is the name of the house elf who serves the Malfoy family?": {"correct": "Dobby", "options": ["Dobby", "Kreacher", "Winky", "Hokey"]},
    "What is the name of the dragon that Harry faces in the Triwizard Tournament?": {"correct": "Hungarian Horntail", "options": ["Hungarian Horntail", "Norwegian Ridgeback", "Swedish Short-Snout", "Chinese Fireball"]},

}

def select_questions():
    selected_questions = random.sample(list(questions.keys()), 5)
    return {question: questions[question] for question in selected_questions}

def quiz():
    selected_questions = select_questions()
    correct_answers = 0
    total_questions = len(selected_questions)

    for question in selected_questions:
        print(question)
        options = selected_questions[question]["options"]
        random.shuffle(options)
        for i, option in enumerate(options):
            print(f"{i+1}. {option}")

        users_answer = int(input("Enter your answer (1-4): \n"))
        if options[users_answer-1] == selected_questions[question]["correct"]:
            correct_answers += 1

    percentage = (correct_answers / total_questions) * 100
    print(f"\nYou got {correct_answers} out of {total_questions} questions correct.")
    print(f"Your score: {percentage:.2f} %")



if __name__ == "__main__":
    main()