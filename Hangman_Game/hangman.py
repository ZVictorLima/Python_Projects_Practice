# Hangman Game 
# This program is meant to train Lists, Sets, and Tuples in Python

from Hangman_Words_List import words

import random

import os

import time

  

hangman_art = {0: ("   ",

                   "   ",

                   "   "),

               1: (" o ",

                   "   ",

                   "   "),

               2: (" o ",

                   " | ",

                   "   "),

                3: (" o ",

                    "/| ",

                    "   "),

                4: (" o ",

                    "/|\\",

                    "   "),

                5: (" o ",

                    "/|\\",

                    "/  "),

                6: (" o ",

                    "/|\\",

                    "/ \\")}

  

def print_hangman(tries):

    print("__________________________")

    for line in hangman_art[tries]:

        print(line)

    print("__________________________")

def display_hint(hint):

    print(" ".join(hint))

  

def display_answer(answer):

    print(" ".join(answer))

  
  

def main():

    tries = 0 # counter for hangman art

    answer = random.choice(words) # pick a random word from the list

    hint = ["_"] * len(answer) # underscore for each letter in the word

    guessed_letters = [] # list of guessed letters

    is_running = True # game loop

  

    print("Welcome to Hangman!")

    while is_running:

        os.system('cls')

        print_hangman(tries)

        display_hint(hint)

        display_answer(answer)

  

        if answer == "".join(hint):  # Compare the joined hint with answer

            print("You win!")

            is_running = False

            continue

  

        guess = input("Guess a letter: ").lower()

        if tries <= 5 :

            if guess in guessed_letters:

                print(f"You already guessed {guess}")

  

            elif guess in answer:

                guessed_letters.append(guess)

                print(f"{guess} is in the word")

                # update hint

                for i in range(len(answer)):

                    if guess == answer[i]:

                        hint[i] = guess

            else:

                guessed_letters.append(guess)

                print(f"{guess} is not in the word")

                tries += 1

        else:

            print("You lose!")

            print(f"The word was {answer}")

            is_running = False

        time.sleep(1)

  

if __name__ == "__main__":

    main()