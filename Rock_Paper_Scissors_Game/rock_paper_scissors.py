# This program is a simple rock, paper, scissors game.

  

import random

  

# Define the possible choices

choices = ("rock", "paper", "scissors")  # tuple because we don't want to change the values

  

# Initialize player choice to None

player_choice = None

  

# Randomly select the computer's choice

computer_choice = random.choice(choices)

  

# Get the player's name

player_name = input("Please input your name: ")

  

# Function to print the choices of both player and computer

def choices_print(player_name, player_choice, computer_choice):

    print(f"{player_name} : {player_choice}")

    print(f"Computer : {computer_choice}")

  

# Loop until the player enters a valid choice

while player_choice not in choices:  # If the player does not enter a valid choice, the loop will continue

    player_choice = input("Rock, Paper or Scissors? ").lower()

  

    # Check if the player's choice is valid

    if player_choice not in choices:

        print("Invalid choice. Please try again")

  

# Determine the result of the game

if player_choice == computer_choice:

    choices_print(player_name, player_choice, computer_choice)

    print("Tie")

elif player_choice == "rock":

    if computer_choice == "paper":

        choices_print(player_name, player_choice, computer_choice)

        print("Computer Wins")

    else:

        choices_print(player_name, player_choice, computer_choice)

        print(f"Player: {player_name} wins")

elif player_choice == "paper":

    if computer_choice == "rock":

        choices_print(player_name, player_choice, computer_choice)

        print(f"Player: {player_name} wins")

    else:

        choices_print(player_name, player_choice, computer_choice)

        print("Computer Wins")

elif player_choice == "scissors":

    if computer_choice == "rock":

        choices_print(player_name, player_choice, computer_choice)

        print("Computer Wins")

    else:

        choices_print(player_name, player_choice, computer_choice)

        print(f"Player: {player_name} wins")