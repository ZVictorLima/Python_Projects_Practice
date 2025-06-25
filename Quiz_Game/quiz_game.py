# Python Quiz Game

# This program is meant to train Lists,Sets and Tuples in Python

# in this case we will be using touple to store the questions and answers

  

questions = ("What is the capital of France?",

              "What is the capital of Spain?",

              "What is the capital of Italy?",

              "What is the capital of Germany?",

              "What is the capital of Portugal?")

  
  

options = (("a. Paris", "b. Madrid", "c. Rome", "d. Berlin"),

           ("a. Madrid", "b. Lisbon", "c. Paris", "d. Berlin"),

           ("a. Madrid", "b. Rome", "c. Berlin", "d. Paris"),

           ("a. Berlin", "b. Rome", "c. Madrid", "d. Lisbon"),

           ("a. Lisbon", "b. Madrid", "c. Paris", "d. Berlin")) # This is a 2D tuple

  

# Correct answers (stored in a tuple)

answers = ("a",  # Capital of France is Paris

           "a",  # Capital of Spain is Madrid

           "b",  # Capital of Italy is Rome

           "a",  # Capital of Germany is Berlin

           "a")  # Capital of Portugal is Lisbon

  

guesses = []

score = 0

question_number = 0

  
  

for question in questions:

    print("+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+")

    print(question)

    for option in options[question_number]:

        print(option)

  

    guess = input("Enter your answer: ").lower() # Get the user's guess

    guesses.append(guess) # Add the guess to the list of guesses

    if guess == answers[question_number]:

        score += 1

        print("Correct!")

    else:

        print("Incorrect!")

    question_number += 1 # Move to the next question

  

print(f" Your score is {score} out of {len(questions)}")