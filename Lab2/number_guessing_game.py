# This program is a number guessing game.
# The computer chooses a random number from 1 to 100.
# The user gets a maximum of 7 attempts to guess it.

import random


def get_guess():
    """Take and validate a guess from the user."""

    while True:
        try:
            guess = int(input("Enter your guess (1-100): "))

            if 1 <= guess <= 100:
                return guess

            print("Please enter a number between 1 and 100.")

        except ValueError:
            print("Invalid input. Please enter an integer.")


def play_game():
    """Run the number guessing game."""

    lower_limit = 1
    upper_limit = 100
    maximum_attempts = 7

    secret_number = random.randint(lower_limit, upper_limit)

    print("===== NUMBER GUESSING GAME =====")
    print(f"I have chosen a number between {lower_limit} and {upper_limit}.")
    print(f"You have {maximum_attempts} attempts to guess it.")

    for attempt in range(1, maximum_attempts + 1):
        print(f"\nAttempt {attempt} of {maximum_attempts}")

        guess = get_guess()

        if guess < secret_number:
            print("Too low!")

        elif guess > secret_number:
            print("Too high!")

        else:
            print(f"Correct! You guessed the number in {attempt} attempts.")
            return

    print(f"\nGame over! You ran out of attempts.")
    print(f"The correct number was {secret_number}.")


play_game()