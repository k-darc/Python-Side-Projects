import random

number = random.randint(1, 100)

print("Welcome to the Numbers Game")
print("I've picked a number between 1 and 100. You have 3 guesses.")
print("I'll give you some hints each time you guess... good luck!")

number_of_guesses = 0

while True:
    guess = int(input("Pick a number: "))
    number_of_guesses += 1

    if guess < number:
        print("Too low. Try again")
    elif guess > number:
        print("Too high. Try again.")
    else:
        print(f"Congratulations! You guesses {number} in {number_of_guesses}!")
        break

# Restart

restart = input("Do you want to play again (Y/N): ")

if restart != "y":
    print("Thank you for playing!")
    break
else:
    number = random.randint(1,100)
    number_of_guesses = 0
    print("I've picked a new number! Let's play again!")