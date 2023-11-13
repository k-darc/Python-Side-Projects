import random

options = ("rock", "paper", "scissors")
playing = True

while playing:

    player = None
    computer = random.choice(options)

    while player not in options:
        player = input("Enter a choice (rock, paper or scissors): ")

    print(f"Player: {player}")
    print(f"Computer: {computer}")

    if player == computer:
        print(f"It's a tie no one has won.", player, "does not beat", computer)
    elif player == "rock" and computer == "scissors":
        print("You win!", player, "beats", computer)
    elif player == "paper" and computer == "rock":
        print(f"You win!", player, "beats", computer)
    elif player == "scissors" and computer == "paper":
        print(f"You win!", player, "beats", computer)
    else:
        print("You have lost", computer, "beats", player)