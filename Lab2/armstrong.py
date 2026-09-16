# This program checks whether a number is an Armstrong number
# and prints all Armstrong numbers within a given range.


def is_armstrong(number):
    """Return True if the given number is an Armstrong number."""

    if number < 0:
        return False

    digits = len(str(number))
    original = number
    total = 0

    while number > 0:
        digit = number % 10
        total += digit ** digits
        number //= 10

    # 0 is also an Armstrong number.
    return total == original


def get_positive_integer(prompt):
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


# Check a single number.
number = get_positive_integer("Enter a number to check: ")

if is_armstrong(number):
    print(f"{number} is an Armstrong number.")
else:
    print(f"{number} is not an Armstrong number.")


# Print Armstrong numbers in a range.
print("\nFind Armstrong numbers in a range")

start = get_positive_integer("Enter the starting value: ")
end = get_positive_integer("Enter the ending value: ")

if start > end:
    start, end = end, start

armstrong_numbers = []

for number in range(start, end + 1):
    if is_armstrong(number):
        armstrong_numbers.append(number)

print(f"Armstrong numbers between {start} and {end}:")

if armstrong_numbers:
    print(*armstrong_numbers)
else:
    print("No Armstrong numbers found in this range.")