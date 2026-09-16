# Lab 6 - Reverse Guessing Game
# The computer guesses the number selected by the user
# using a binary-search style strategy.


def get_integer(prompt):
    """Take and validate an integer."""

    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input. Please enter an integer.")


def get_feedback():
    """Take and validate the user's feedback."""

    while True:
        feedback = input(
            "Enter feedback (h = too high, l = too low, c = correct): "
        ).lower()

        if feedback in ("h", "l", "c"):
            return feedback

        print("Invalid feedback. Enter h, l, or c.")


def reverse_guessing_game():
    """Run the computer guessing game."""

    print("===== REVERSE GUESSING GAME =====")

    lower = get_integer("Enter the lower limit: ")
    upper = get_integer("Enter the upper limit: ")

    if lower >= upper:
        print("Lower limit must be smaller than upper limit.")
        return

    print(f"\nThink of a number between {lower} and {upper}.")
    print("I will try to guess it using binary search.")

    attempts = 0

    while lower <= upper:

        guess = (lower + upper) // 2
        attempts += 1

        print(f"\nMy guess is: {guess}")

        feedback = get_feedback()

        if feedback == "c":
            print(f"I guessed your number in {attempts} guesses!")
            return

        elif feedback == "h":
            upper = guess - 1

        elif feedback == "l":
            lower = guess + 1

    print("\nYour feedback was inconsistent.")
    print("The possible range became empty.")


if __name__ == "__main__":
    reverse_guessing_game()