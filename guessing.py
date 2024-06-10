import random

def main():
    number = random.randint(1, 100)

    print("Welcome to the Numbers Game")
    print("I've picked a number between 1 and 100.")
    print("I'll give you some hints each time you guess... good luck!")

    guesses = 0

    while True:
        guess = int(input("Pick a number: "))
        guesses += 1

        if guess < number:
            print("Too low. Try again")
        elif guess > number:
            print("Too high. Try again.")
        else:
            print(f"Congratulations! You guesses {number} in {guesses}!")
            break

    # Restart
    play_again = input("Do you want to play again (Y/N): ").lower()

    if play_again != "y":
        print("Thank you for playing!")
    else:
        number = random.randint(1, 100)
        guesses = 0
        print("I've picked a new number! Let's play again!")
        main()
main()