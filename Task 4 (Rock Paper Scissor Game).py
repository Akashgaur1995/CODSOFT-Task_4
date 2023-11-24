import random

user_choice = input("Enter your choice (rock, paper, scissors): ")
possible_choices = ["rock", "paper", "scissors"]
computer_choice = random.choice(possible_choices)
print(f"You chose {user_choice}, computer chose {computer_choice}")

if user_choice == computer_choice:
    print(f"Both players selected {user_choice}.", " It's a tie!😐")
elif user_choice == "rock":
    if computer_choice == "scissors":
        print("Rock smashes Scissors! You win!😃✌")
    else:
        print("Paper covers Rock! You lose.😞")
elif user_choice == "paper":
    if computer_choice == "rock":
        print("Paper covers Rock! You win!😃✌")
    else:
        print("Scissors cuts Paper! You lose.😞")
elif user_choice == "scissors":
    if computer_choice == "paper":
        print("Scissors cuts Paper! You win!😃✌")
    else:
        print("Rock smashes Scissors! You lose.😞")