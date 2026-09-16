# Lab 6 - Guessing Game with Hints and Scoring
# The computer selects a random number and gives
# even/odd and multiple-of-5 hints after wrong guesses.


import random


def get_guess(lower, upper):
    """Take and validate the user's guess."""

    while True:
        try:
            guess = int(input(f"Enter your guess ({lower}-{upper}): "))

            if lower <= guess <= upper:
                return guess

            print(f"Please enter a number between {lower} and {upper}.")

        except ValueError:
            print("Invalid input. Please enter an integer.")


def guessing_game():
    """Run the guessing game."""

    lower = 1
    upper = 100
    maximum_attempts = 7

    secret_number = random.randint(lower, upper)
    score = 100

    print("\n===== GUESSING GAME WITH HINTS =====")
    print(f"I selected a number between {lower} and {upper}.")
    print(f"You have {maximum_attempts} attempts.")
    print("You start with 100 points.")
    print("Each wrong guess costs 10 points.")

    for attempt in range(1, maximum_attempts + 1):

        print(f"\nAttempt {attempt} of {maximum_attempts}")

        guess = get_guess(lower, upper)

        if guess == secret_number:
            print("\nCorrect!")
            print(f"You guessed the number in {attempt} attempts.")
            print(f"Final score: {score}")
            return

        score -= 10

        if guess < secret_number:
            print("Too low!")
        else:
            print("Too high!")

        # Even / odd hint
        if secret_number % 2 == 0:
            print("Hint: The secret number is even.")
        else:
            print("Hint: The secret number is odd.")

        # Multiple of 5 hint
        if secret_number % 5 == 0:
            print("Hint: The secret number is a multiple of 5.")
        else:
            print("Hint: The secret number is not a multiple of 5.")

    print("\nYou lost!")
    print(f"The secret number was {secret_number}.")
    print("Final score: 0")


if __name__ == "__main__":
    guessing_game()