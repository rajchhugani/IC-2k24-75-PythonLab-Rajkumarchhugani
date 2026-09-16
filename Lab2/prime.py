# This program checks whether a number is prime
# and prints all prime numbers up to a given limit.


def is_prime(number):
    """Return True if the given number is prime."""

    if number < 2:
        return False

    if number == 2:
        return True

    if number % 2 == 0:
        return False

    divisor = 3

    # Only test divisors up to the square root of the number.
    while divisor * divisor <= number:
        if number % divisor == 0:
            return False
        divisor += 2

    return True


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


# Check whether a single number is prime.
number = get_non_negative_integer("Enter a number to check: ")

if is_prime(number):
    print(f"{number} is a prime number.")
else:
    print(f"{number} is not a prime number.")


# Print all prime numbers up to a given limit.
print("\nFind prime numbers up to a limit")

limit = get_non_negative_integer("Enter the limit: ")

prime_numbers = []

for number in range(2, limit + 1):
    if is_prime(number):
        prime_numbers.append(number)

print(f"Prime numbers up to {limit}:")

if prime_numbers:
    print(*prime_numbers)
else:
    print("No prime numbers found.")