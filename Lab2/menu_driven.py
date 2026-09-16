# This program combines the Lab 2 programs into a menu-driven application.


def is_armstrong(number):
    """Return True if the number is an Armstrong number."""

    if number < 0:
        return False

    original = number
    digits = len(str(number))
    total = 0

    if number == 0:
        return True

    while number > 0:
        digit = number % 10
        total += digit ** digits
        number //= 10

    return total == original


def is_prime(number):
    """Return True if the number is prime."""

    if number < 2:
        return False

    if number == 2:
        return True

    if number % 2 == 0:
        return False

    divisor = 3

    while divisor * divisor <= number:
        if number % divisor == 0:
            return False
        divisor += 2

    return True


def is_perfect(number):
    """Return True if the number is a perfect number."""

    if number <= 1:
        return False

    divisor_sum = 1
    divisor = 2

    while divisor * divisor <= number:
        if number % divisor == 0:
            divisor_sum += divisor

            other_divisor = number // divisor

            if other_divisor != divisor:
                divisor_sum += other_divisor

        divisor += 1

    return divisor_sum == number


def is_number_palindrome(number):
    """Check whether a number is a palindrome using arithmetic."""

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
    """Return True if the string is a palindrome."""

    text = text.lower()
    return text == text[::-1]


def fibonacci_loop(n):
    """Return the first n Fibonacci terms using a loop."""

    series = []
    first = 0
    second = 1

    for _ in range(n):
        series.append(first)
        first, second = second, first + second

    return series


def fibonacci_recursive(n):
    """Return the nth Fibonacci number using recursion."""

    if n <= 1:
        return n

    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)


def get_integer(prompt):
    """Take and validate an integer."""

    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input. Please enter an integer.")


def get_positive_integer(prompt):
    """Take and validate a positive integer."""

    while True:
        number = get_integer(prompt)

        if number > 0:
            return number

        print("Please enter a positive integer.")


def print_patterns(rows):
    """Print the three required patterns."""

    print("\n1. Right-Angled Triangle")

    for row in range(1, rows + 1):
        for _ in range(row):
            print("*", end=" ")
        print()

    print("\n2. Number Pattern")

    for row in range(1, rows + 1):
        for number in range(1, row + 1):
            print(number, end=" ")
        print()

    print("\n3. Centered Pyramid")

    for row in range(1, rows + 1):
        for _ in range(rows - row):
            print(" ", end=" ")

        for _ in range(2 * row - 1):
            print("*", end=" ")

        print()


def main():
    """Run the menu-driven application."""

    while True:
        print("\n========== LAB 2 MENU ==========")
        print("1. Armstrong Number")
        print("2. Prime Number")
        print("3. Perfect Number")
        print("4. Palindrome")
        print("5. Fibonacci Series")
        print("6. Pattern Printing")
        print("7. Exit")
        print("================================")

        choice = input("Enter your choice: ")

        if choice == "1":
            number = get_integer("Enter a number: ")

            if number < 0:
                print("Please enter a non-negative number.")
                continue

            if is_armstrong(number):
                print(f"{number} is an Armstrong number.")
            else:
                print(f"{number} is not an Armstrong number.")

        elif choice == "2":
            number = get_integer("Enter a number: ")

            if is_prime(number):
                print(f"{number} is a prime number.")
            else:
                print(f"{number} is not a prime number.")

        elif choice == "3":
            number = get_positive_integer("Enter a positive number: ")

            if is_perfect(number):
                print(f"{number} is a perfect number.")
            else:
                print(f"{number} is not a perfect number.")

        elif choice == "4":
            print("\n1. Number Palindrome")
            print("2. String Palindrome")

            palindrome_choice = input("Enter your choice: ")

            if palindrome_choice == "1":
                number = get_integer("Enter a non-negative number: ")

                if number < 0:
                    print("Please enter a non-negative number.")
                elif is_number_palindrome(number):
                    print(f"{number} is a palindrome.")
                else:
                    print(f"{number} is not a palindrome.")

            elif palindrome_choice == "2":
                text = input("Enter a string: ")

                if is_string_palindrome(text):
                    print(f'"{text}" is a palindrome.')
                else:
                    print(f'"{text}" is not a palindrome.')

            else:
                print("Invalid palindrome choice.")

        elif choice == "5":
            n = get_positive_integer("Enter the number of Fibonacci terms: ")

            print("\nFibonacci using loop:")
            print(*fibonacci_loop(n))

            if n <= 20:
                print("\nFibonacci using recursion:")
                recursive_series = [
                    fibonacci_recursive(i) for i in range(n)
                ]
                print(*recursive_series)
            else:
                print("\nRecursive version skipped for large n.")

        elif choice == "6":
            rows = get_positive_integer("Enter the number of rows: ")
            print_patterns(rows)

        elif choice == "7":
            print("Exiting the Lab 2 application. Goodbye!")
            break

        else:
            print("Invalid menu choice. Please select an option from 1 to 7.")


if __name__ == "__main__":
    main()