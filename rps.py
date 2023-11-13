import random

options = ("rock", "paper", "scissors")
playing = True

while playing:

    player = None
    computer = random.choice(options)

    player = input("Enter a choice (rock, paper or scissors): ")

    print(f"Player: {player}")
    print(f"Computer: {computer}")

    if player == computer:
        print("It's a tie no one has won.")
    elif player == "rock" and computer == "scissors":
        print("You win!")
    elif player == "paper" and computer == "rock":
        print(f"You win!")
    elif player == "scissors" and computer == "paper":
        print(f"You win!")
    else:
        print("You have lost")
