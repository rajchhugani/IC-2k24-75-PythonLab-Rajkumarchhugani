# This program prints the Fibonacci series using a loop and recursion.
# It also counts the function calls made by the recursive version.


def fibonacci_loop(n):
    """Return the first n Fibonacci terms using a loop."""

    series = []
    first = 0
    second = 1

    for _ in range(n):
        series.append(first)
        first, second = second, first + second

    return series


recursive_calls = 0


def fibonacci_recursive(n):
    """Return the nth Fibonacci number using recursion."""

    global recursive_calls
    recursive_calls += 1

    if n <= 1:
        return n

    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)


def fibonacci_recursive_series(n):
    """Generate the first n Fibonacci terms using recursion."""

    return [fibonacci_recursive(i) for i in range(n)]


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


# Get the number of terms.
n = get_positive_integer("Enter the number of Fibonacci terms: ")

# Loop-based version.
loop_series = fibonacci_loop(n)

print("\nFibonacci series using loop:")
print(*loop_series)


# Recursive version.
recursive_calls = 0
recursive_series = fibonacci_recursive_series(n)

print("\nFibonacci series using recursion:")
print(*recursive_series)

print("Number of recursive function calls:", recursive_calls)