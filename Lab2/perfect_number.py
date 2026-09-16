# This program checks whether a number is a perfect number
# and prints all perfect numbers up to a given limit.


def is_perfect(number):
    """Return True if the given number is a perfect number."""

    if number <= 1:
        return False

    divisor_sum = 1

    # Check possible proper divisors up to the square root.
    divisor = 2

    while divisor * divisor <= number:
        if number % divisor == 0:
            divisor_sum += divisor

            other_divisor = number // divisor

            if other_divisor != divisor:
                divisor_sum += other_divisor

        divisor += 1

    return divisor_sum == number


def get_positive_integer(prompt):
    """Take and validate a positive integer from the user."""

    while True:
        try:
            number = int(input(prompt))

            if number <= 0:
                print("Please enter a positive integer.")
            else:
                return number

        except ValueError:
            print("Invalid input. Please enter an integer.")


# Check whether a single number is perfect.
number = get_positive_integer("Enter a number to check: ")

if is_perfect(number):
    print(f"{number} is a perfect number.")
else:
    print(f"{number} is not a perfect number.")


# Print all perfect numbers up to a given limit.
print("\nFind perfect numbers up to a limit")

limit = get_positive_integer("Enter the limit: ")

perfect_numbers = []

for number in range(2, limit + 1):
    if is_perfect(number):
        perfect_numbers.append(number)

print(f"Perfect numbers up to {limit}:")

if perfect_numbers:
    print(*perfect_numbers)
else:
    print("No perfect numbers found.")