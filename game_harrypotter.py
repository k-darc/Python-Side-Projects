import random

def main():
    print(f"Welcome to the Harry Potter Quiz! (questions provided by ChatGPT)")
    print(f"Answer 5 questions by typing in the correct number and hitting Enter.")
    print(f"Let's start!\n")
    quiz()

questions = {
    "What is the name of Harry Potter's owl?": {"correct": "Hedwig", "options": ["Hedwig", "Scabbers", "Crookshanks", "Fawkes"]},
    "What position does Harry play on his Quidditch team?": {"correct": "Seeker", "options": ["Seeker", "Chaser", "Keeper", "Beater"]},
    "Who is the Half-Blood Prince?": {"correct": "Severus Snape", "options": ["Severus Snape", "Albus Dumbledore", "Tom Riddle", "Sirius Black"]},
    "What is the name of Hagrid's three-headed dog?": {"correct": "Fluffy", "options": ["Fluffy", "Norbert", "Aragog", "Buckbeak"]},
    "What is the name of the train that takes students to Hogwarts?": {"correct": "Hogwarts Express", "options": ["Hogwarts Express", "Knight Bus", "Thestral", "Ford Anglia"]},
    "What is the name of the Weasley twins?": {"correct": "Fred and George", "options": ["Fred and George", "Ron and Harry", "Bill and Charlie", "Percy and Oliver"]},
    "Who killed Sirius Black?": {"correct": "Bellatrix Lestrange", "options": ["Bellatrix Lestrange", "Voldemort", "Peter Pettigrew", "Lucius Malfoy"]},
    "What is the spell to summon an object?": {"correct": "Accio", "options": ["Accio", "Alohomora", "Expelliarmus", "Expecto Patronum"]},
    "Who is the headmaster of Hogwarts in the first book?": {"correct": "Albus Dumbledore", "options": ["Albus Dumbledore", "Severus Snape", "Minerva McGonagall", "Rubeus Hagrid"]},
    "What is the core of Harry's wand?": {"correct": "Phoenix Feather", "options": ["Phoenix Feather", "Dragon Heartstring", "Unicorn Hair", "Thestral Tail Hair"]},
    "What is the name of Harry's father?": {"correct": "James Potter", "options": ["James Potter", "Sirius Black", "Severus Snape", "Jack Potter"]},
    "Who is the author of the Harry Potter series?": {"correct": "J.K. Rowling", "options": ["J.K. Rowling", "J. R. R. Tolkein", "George R.R. Martin", "Terry Pratchett"]},
    "What is the name of Harry's best friends?": {"correct": "Hermione Granger and Ron Weasley", "options": ["Hermione Granger and Ron Weasley", "Hermione Granger and Neville Longbottom", "Ron Weasley and Draco Malfoy", "Ron Weasley and Neville Longbottom"]},
    "What creature does Hagrid raise illegal in the first book?": {"correct": "Norwegian Ridgeback", "options": ["Norwegian Ridgeback", "Hungarian Horntail", "Swedish Short-Snout", "Peruvian Vipertooth"]},
    "What is the name of the house elf who serves the Malfoy family?": {"correct": "Dobby", "options": ["Dobby", "Kreacher", "Winky", "Hokey"]},
    "What magical object can make the owner invisible?": {"correct": "Invisibility Cloak", "options": ["Invisibility Cloak", "Sneakoscope", "Time-Turner", "Remembrall"]},
    "Who teaches Defense Against the Dark Arts in Harry's second year at Hogwarts?": {"correct": "Gilderoy Lockhart", "options": ["Gilderoy Lockhart", "Severus Snape", "Remus Lupin", "Quirinus Quirrell"]},
    "What is the name of one of the schools rivaling Hogwarts in the Triwizard Tournament?": {"correct": "Durmstrang Institute", "options": ["Durmstrang Institute", "Dragonegg Academy of Magic", "Ilvermorny School of Witchcraft and Wizardry", "Mahoutokoro School of Magic"]},
    "What is the magical plant that cries loudly?": {"correct": "Mandrake", "options": ["Mandrake", "Mimbulus Mimbletonia", "Devil's Snare", "Whomping Willow"]},
    "What is the name of the village where Harry grew up with the Dursleys?": {"correct": "Little Whinging", "options": ["Little Whinging", "Godric's Hollow", "Hogsmeade", "Ottery St. Catchpole"]},
    "What is the name of the potion that grants the drinker luck for a period of time?": {"correct": "Liquid Luck (Felix Felicis)", "options": ["Liquid Luck (Felix Felicis)", "Polyjuice Potion", "Veritaserum", "Treacle Tart (Lucky Tart)"]},
    "What is the name of the magical device used to store and view memories?": {"correct": "Pensieve", "options": ["Pensieve", "Time-Turner", "Remembrall", "Deluminator"]},
    "What is the name of the ghost who haunts the girls' bathroom at Hogwarts?": {"correct": "Moaning Myrtle", "options": ["Moaning Myrtle", "The Bloody Baron", "Nearly Headless Nick", "The Grey Lady"]},
    "What is the name of the street where the Leaky Cauldron is located?": {"correct": "Diagon Alley", "options": ["Diagon Alley", "Knockturn Alley", "Hogsmeade", "Privet Drive"]},
    "What is the name of the wizard bank in London?": {"correct": "Gringotts", "options": ["Gringotts", "The Ministry of Magic", "St. Mungo's Hospital for Magical Maladies and Injuries", "Ollivanders"]},
    "Who is the captain of the Slytherin Quidditch team in Harry's first year at Hogwarts?": {"correct": "Marcus Flint", "options": ["Marcus Flint", "Draco Malfoy", "Vincent Crabbe", "Gregory Goyle"]},
    "What magical object shows the locations of people in Hogwarts?": {"correct": "Marauder's Map", "options": ["Marauder's Map", "The Mirror of Erised", "The Sword of Gryffindor", "The Resurrection Stone"]},
    "What color is Hermione's cat?": {"correct": "Orange", "options": ["Orange", "Black and white", "Brown", "Brown and white"]},
    "What creature serves as the emblem for Hufflepuff house?": {"correct": "Badger", "options": ["Badger", "Lion", "Eagle", "Snake"]},
    "What creature serves as the emblem for Ravenclaw house?": {"correct": "Eagle", "options": ["Eagle", "Badger", "Lion", "Snake"]},
    "Who is the Divination professor at Hogwarts during Harry's third year?": {"correct": "Sybill Trelawney", "options": ["Sybill Trelawney", "Firenze", "Bathilda Bagshot", "Xenophilius Lovegood"]},
    "What is the name of the popular pub located in Hogsmeade?": {"correct": "The Three Broomsticks", "options": ["The Three Broomsticks", "The Hog's Head", "The Leaky Cauldron", "The Hogsmeade Inn"]},
    "What is the name of the mermaid colony near Hogwarts?": {"correct": "The Merpeople's Village", "options": ["The Merpeople's Village", "The Black Lake Colony", "The Siren's Cove", "The Selkie Sanctuary"]},
    "What is the name of the house elf who serves the Black family?": {"correct": "Kreacher", "options": ["Kreacher", "Dobby", "Winky", "Hokey"]},
    "What is the name of the sport played on broomsticks in the wizarding world?": {"correct": "Quidditch", "options": ["Quidditch", "Broomstick Racing", "Broomstick Polo", "Broomstick Football"]},
    "What is the name of the magical village near Hogwarts?": {"correct": "Hogsmeade", "options": ["Hogsmeade", "Diagon Alley", "Godric's Hollow", "Ottery St. Catchpole"]},
    "Who is the founder of Gryffindor house?": {"correct": "Godric", "options": ["Godric", "Salazar", "Helga", "Rowena"]},
    "What is the magical device Mrs. Weasley uses that shows where family members are?": {"correct": "A clock", "options": ["A clock", "A crystal ball", "A Sneakoscope", "Marauder's Map"]},
    "What is the name of the magical creature that can transform into an animal?": {"correct": "Animagus", "options": ["Animagus", "Werewolf", "Boggart", "Hippogriff"]},
    "What is the name of the prison for wizards and witches?": {"correct": "Azkaban", "options": ["Azkaban", "Nurmengard", "Gringotts", "St. Mungo's Hospital for Magical Maladies and Injuries"]},
    "What is the name of the potion that grants the drinker the ability to transform into someone else?": {"correct": "Polyjuice Potion", "options": ["Polyjuice Potion", "Veritaserum", "Amortentia", "Felix Felicis"]},
    "What is the name of Hagrid's giant half-brother?": {"correct": "Grawp", "options": ["Grawp", "Fang", "Buckbeak", "Aragog"]},
    "What is the name of the ghost who haunts the Gryffindor common room?": {"correct": "Nearly Headless Nick", "options": ["Nearly Headless Nick", "The Bloody Baron", "Moaning Myrtle", "The Fat Friar"]},
    "What is the name of the wizarding newspaper?": {"correct": "The Daily Prophet", "options": ["The Daily Prophet", "The Quibbler", "Witch Weekly", "The Daily Bugle"]},
    "What is the name of the ghost who haunts the Ravenclaw common room?": {"correct": "The Grey Lady", "options": ["The Grey Lady", "Nearly Headless Nick", "Moaning Myrtle", "The Bloody Baron"]},
    "What is the name of the magical village where Harry's parents were killed?": {"correct": "Godric's Hollow", "options": ["Godric's Hollow", "Hogsmeade", "Diagon Alley", "Ottery St. Catchpole"]},
    "What is the name of Hermione's cat?": {"correct": "Crookshanks", "options": ["Crookshanks", "Mrs. Norris", "Arnold", "Trevor"]},
    "What animal does Rita Skeeter transform into?": {"correct": "A bug", "options": ["A bug", "A cat", "A rat", "A butterfly"]},
    "What is Dumbledore's middle name?": {"correct": "All of the above", "options": ["All of the above", "Percival ", "Brian", "Wulfric"]},
    "What is the name of the curse that kills with a flash of green light?": {"correct": "Avada Kedavra", "options": ["Avada Kedavra", "Cruciatus Curse", "Imperius Curse", "Stupefy"]},
    "What is the name of Voldermort's snake?": {"correct": "Nagini", "options": ["Nagini", "Buckbeak", "Aragog", "Fang"]},
    "Who is the Potions Master at Hogwarts during Harry's time there?": {"correct": "Severus Snape", "options": ["Severus Snape", "Horace Slughorn", "Pomona Sprout", "Filius Flitwick"]},
    "What is the name of the organization founded by Albus Dumbledore to fight Voldemort?": {"correct": "The Order of the Phoenix", "options": ["The Order of the Phoenix", "The Death Eaters", "Dumbledore's Army", "The Ministry of Magic"]},
    "What enchanted objects does Dumbledore's Army use to communicate?": {"correct": "Coins", "options": ["Coins", "Letters", "Remembralls", "Buttons"]},
    "What is the name of the device used to travel back in time?": {"correct": "Time-Turner", "options": ["Time-Turner", "Portkey", "Apparition", "Floo Powder"]},
    "What is the name of the object used to contain a fragment of the owners soul?": {"correct": "Horcrux", "options": ["Horcrux", "Portkey", "Pensieve", "Deluminator"]},
    "Who runs the Wizard bank in London?": {"correct": "Goblins", "options": ["Goblins", "Dwarfs", "Elves", "Muggles"]},
    "What is the name of the dragon that Harry faces in the Triwizard Tournament?": {"correct": "Hungarian Horntail", "options": ["Hungarian Horntail", "Norwegian Ridgeback", "Swedish Short-Snout", "Chinese Fireball"]},
    "What is the name of the spell that unlocks doors?": {"correct": "Alohomora", "options": ["Alohomora", "Accio", "Expelliarmus", "Expecto Patronum"]},
    "What is the name of the creature that guards the entrance to Gryffindor Tower?": {"correct": "The Fat Lady", "options": ["The Fat Lady", "The Grey Lady", "Nearly Headless Nick", "The Bloody Baron"]},
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