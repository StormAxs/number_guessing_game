from multiprocessing.connection import answer_challenge
from os import killpg
import random
from random import randint

DEBUG = False

def guess_game(diff):
    guess_count = 0
    if diff == 1:
        guess_count += 10
    elif diff == 2:
        guess_count += 5
    elif diff == 3:
        guess_count += 3

    answer = randint(1, 100)
    if DEBUG:
        print(answer)

    while guess_count != 0:
        guess = int(input("Enter your guess: "))
        if guess > answer:
            print(f"Incorrect! The number is less than {guess}")
            guess_count -=1
        elif guess < answer:
            print(f"Incorrect! The number is greater than {guess}")
            guess_count -=1
        elif answer == guess:
            print("Congratulations! You guessed the correct number")
            return "WIN!"

    if guess_count == 0:
        print("GameOver!")


print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100")

print("Please select the difficulty level: ")
print("1. Easy (10 chances)")
print("2. Medium (5 chances)")
print("3. Hard (3 chances)")
difficulty = int(input("Enter your choice: "))

if 0 > difficulty > 3:
    difficulty = None
    if None:
        raise Exception("None")


if difficulty == 1:
    difficulty_name = "Easy"
elif difficulty == 2:
    difficulty_name = "Medium"
elif difficulty == 3:
    difficulty_name = "Hard"
else:
    difficulty_name = None

if difficulty_name:
    print(f"Great! You have selected the {difficulty_name} difficulty level.")
else:
    print("Invalid choice. Please enter 1 for Easy, 2 for Medium, or 3 for Hard.")


guess_game(difficulty)