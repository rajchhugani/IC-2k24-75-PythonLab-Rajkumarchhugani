# This program checks whether a number and a string are palindromes.


def is_number_palindrome(number):
    """Return True if the number is a palindrome using arithmetic operations."""

    if number < 0:
        return False

    original = number
    reversed_number = 0

    while number > 0:
        digit = number % 10
        reversed_number = reversed_number * 10 + digit
        number //= 10

    return original == reversed_number


def is_string_palindrome(text):
    """Return True if the string reads the same forwards and backwards."""

    text = text.lower()
    return text == text[::-1]


def get_non_negative_integer(prompt):
    """Take and validate a non-negative integer from the user."""

    while True:
        try:
            number = int(input(prompt))

            if number < 0:
                print("Please enter a non-negative integer.")
            else:
                return number

        except ValueError:
            print("Invalid input. Please enter an integer.")


# Number palindrome check
number = get_non_negative_integer("Enter a number to check: ")

if is_number_palindrome(number):
    print(f"{number} is a palindrome.")
else:
    print(f"{number} is not a palindrome.")


# String palindrome check
text = input("\nEnter a string to check: ")

if is_string_palindrome(text):
    print(f'"{text}" is a palindrome.')
else:
    print(f'"{text}" is not a palindrome.')