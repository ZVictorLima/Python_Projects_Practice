# Program to simulate a slot machine with 3 reels

from Python_Projects_Practice.Banking_Program import Banking_Project as bp  # Importing the banking project for deposit and withdraw functions

# import Banking_Project as bp # this has the functions to deposit and withdraw money

import random

import time

  

reel_options = ["🍒","🔔","💀","👀"]

  

def pull_the_lever_gronk(balance):

    if balance < 1:

        print("Insufficient funds")

        return 0

    elif balance >= 1:

        balance -= 1

        print("Spinning...")

        time.sleep(2)

        won = print_slot_machine(balance)

        balance += won

        return balance

  

def print_slot_machine(balance):

    reel1 = random.choice(reel_options)

    reel2 = random.choice(reel_options)

    reel3 = random.choice(reel_options)

    print("***********************")

    print(f"  {reel1}  |  {reel2}  |  {reel3}  ")

    print("***********************")

    if reel1 == reel2 == reel3:

        print("You win!")

        return  10

    else:

        print("You lose!")

        return 0

    print(f"Your balance is now: ${balance}")

  

def withdraw_money(balance):

    amount_to_withdraw = bp.withdraw(balance)

    # Check if withdrawal was successful by seeing if it's a positive number

    if isinstance(amount_to_withdraw, (int, float)) and amount_to_withdraw > 0:

        balance -= amount_to_withdraw

        print(f"Withdrew ${amount_to_withdraw}. New balance: ${balance}")

    return balance

  
  

def deposit_money(balance):

    amount_to_deposit = bp.deposit(balance)

    # Ensure the returned value is a valid number (not a string)

    if isinstance(amount_to_deposit, (int, float)):

        balance += amount_to_deposit

        print(f"Deposited ${amount_to_deposit}. New balance: ${balance}")

    else:

        print(amount_to_deposit)  # Likely to print "Invalid Amount"

    return balance

  
  
  

def main():

    balance = 0  # Starting balance

    is_running = True

  

    print("Welcome to the slot machine!")

    print(f"Your Current balance is: ${balance}")

    print("Each pull costs $1")

  

    while is_running:

        print(f"Your Current balance is: ${balance}")

        user_choice = input("What would you like to do? (1. Pull the lever, 2. Deposit, 3. Withdraw, 4. Quit): ")

        match user_choice:

            case "1":

                balance = pull_the_lever_gronk(balance)  # Update balance here

            case "2":

                balance = deposit_money(balance)  # Update balance with new deposit

            case "3":

                balance = withdraw_money(balance)  # Update balance with new withdrawal

            case "4":

                is_running = False

            case _:

                print("Invalid choice")

  
  

if __name__ == "__main__":

    main()