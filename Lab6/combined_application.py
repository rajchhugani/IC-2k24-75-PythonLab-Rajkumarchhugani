# Lab 6 - Combined Application
# Combines ATM, Student Grade Calculator,
# and Guessing Game with Hints and Scoring.


import random


# ============================================================
# ATM
# ============================================================

def atm_application():
    """Run the ATM application."""

    balance = 5000
    pin = "1234"

    entered_pin = input("Enter your PIN: ")

    if entered_pin != pin:
        print("Incorrect PIN. Access denied.")
        return

    while True:
        print("\n===== ATM =====")
        print("1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Change PIN")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            print(f"Current balance: ₹{balance:.2f}")

        elif choice == "2":
            try:
                amount = float(input("Enter deposit amount: "))

                if amount <= 0:
                    print("Amount must be greater than zero.")
                else:
                    balance += amount
                    print(f"New balance: ₹{balance:.2f}")

            except ValueError:
                print("Invalid amount.")

        elif choice == "3":
            try:
                amount = float(input("Enter withdrawal amount: "))

                if amount <= 0:
                    print("Amount must be greater than zero.")

                elif amount > balance:
                    print("Transaction rejected.")
                    print("Insufficient balance.")

                else:
                    balance -= amount
                    print(f"Withdrawal successful.")
                    print(f"Remaining balance: ₹{balance:.2f}")

            except ValueError:
                print("Invalid amount.")

        elif choice == "4":
            current_pin = input("Enter current PIN: ")

            if current_pin == pin:
                new_pin = input("Enter new 4-digit PIN: ")

                if len(new_pin) == 4 and new_pin.isdigit():
                    pin = new_pin
                    print("PIN changed successfully.")
                else:
                    print("PIN must contain exactly 4 digits.")
            else:
                print("Incorrect current PIN.")

        elif choice == "5":
            print("Exiting ATM...")
            return

        else:
            print("Invalid ATM choice.")


# ============================================================
# GRADE CALCULATOR
# ============================================================

def get_mark(subject_number):
    """Take and validate marks between 0 and 100."""

    while True:
        try:
            mark = float(input(f"Enter marks for subject {subject_number}: "))

            if 0 <= mark <= 100:
                return mark

            print("Marks must be between 0 and 100.")

        except ValueError:
            print("Invalid input. Please enter a number.")


def calculate_grade(average):
    """Calculate grade from average marks."""

    if average >= 90:
        return "A"
    elif average >= 75:
        return "B"
    elif average >= 60:
        return "C"
    elif average >= 40:
        return "D"
    else:
        return "F"


def grade_application():
    """Run the grade calculator."""

    last_student = None

    while True:
        print("\n===== GRADE CALCULATOR =====")
        print("1. Enter marks for a new student")
        print("2. View grade of last entered student")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":

            marks = []

            for subject in range(1, 6):
                marks.append(get_mark(subject))

            average = sum(marks) / 5
            grade = calculate_grade(average)

            last_student = {
                "marks": marks,
                "average": average,
                "grade": grade
            }

            print("\nStudent data saved.")
            print(f"Average: {average:.2f}")
            print(f"Grade: {grade}")

        elif choice == "2":

            if last_student is None:
                print("No student data has been entered.")
            else:
                print("\n===== LAST STUDENT =====")
                print("Marks:", *last_student["marks"])
                print(f"Average: {last_student['average']:.2f}")
                print(f"Grade: {last_student['grade']}")

        elif choice == "3":
            print("Exiting Grade Calculator...")
            return

        else:
            print("Invalid choice.")


# ============================================================
# GUESSING GAME
# ============================================================

def guessing_game():
    """Run the guessing game with hints and scoring."""

    lower = 1
    upper = 100
    maximum_attempts = 7

    secret_number = random.randint(lower, upper)
    score = 100

    print("\n===== GUESSING GAME =====")
    print("I selected a number between 1 and 100.")
    print("You have 7 attempts.")
    print("You start with 100 points.")
    print("Each wrong guess costs 10 points.")

    for attempt in range(1, maximum_attempts + 1):

        print(f"\nAttempt {attempt} of {maximum_attempts}")

        try:
            guess = int(input("Enter your guess (1-100): "))

            if guess < lower or guess > upper:
                print("Please enter a number between 1 and 100.")
                continue

        except ValueError:
            print("Invalid input. Please enter an integer.")
            continue

        if guess == secret_number:
            print("\nCorrect!")
            print(f"You guessed it in {attempt} attempts.")
            print(f"Final score: {score}")
            return

        score -= 10

        if guess < secret_number:
            print("Too low!")
        else:
            print("Too high!")

        if secret_number % 2 == 0:
            print("Hint: The number is even.")
        else:
            print("Hint: The number is odd.")

        if secret_number % 5 == 0:
            print("Hint: The number is a multiple of 5.")
        else:
            print("Hint: The number is not a multiple of 5.")

    print("\nYou lost!")
    print(f"The secret number was {secret_number}.")
    print("Final score: 0")


# ============================================================
# TOP-LEVEL MENU
# ============================================================

def main():
    """Run the combined application."""

    while True:

        print("\n================================")
        print("       COMBINED APPLICATION")
        print("================================")
        print("1. ATM")
        print("2. Grade Calculator")
        print("3. Guessing Game")
        print("4. Exit")
        print("================================")

        choice = input("Enter your choice: ")

        if choice == "1":
            atm_application()

        elif choice == "2":
            grade_application()

        elif choice == "3":
            guessing_game()

        elif choice == "4":
            print("Exiting Combined Application. Goodbye!")
            break

        else:
            print("Invalid choice. Please select 1, 2, 3, or 4.")


if __name__ == "__main__":
    main()
    