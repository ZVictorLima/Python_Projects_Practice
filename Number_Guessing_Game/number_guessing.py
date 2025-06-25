#Guessing game using random number generator

  

# Importing the random module

import random

  

# Lets set the range of the random number

min = 1

max = 100

# Lets also keep track of guesses

guesses_num = 0

  

# Lets initialize the guess (otherwise while loop will throw an error)

guess = None

  

# Now create a random number

random_number = random.randint(min,max)

  

# Now that we have or number generated lets create the guessign game

print("Welcome to the number guessing game")

print(f"I have chose a number from {min} to {max}")

  

while guess != random_number:

    guess = int(input("Enter your guess: "))

    guesses_num += 1

    if guess > random_number:

        print("Too high")

    elif guess < random_number:

        print("Too low")

    else:

        print(f"Congratulations! You guessed the number in {guesses_num} tries")

        break