# This program prints a butterfly star pattern.


def get_positive_integer(prompt):
    """Take and validate a positive integer from the user."""

    while True:
        try:
            n = int(input(prompt))

            if n <= 0:
                print("Please enter a positive integer.")
            else:
                return n

        except ValueError:
            print("Invalid input. Please enter an integer.")


n = get_positive_integer("Enter the number of rows: ")


# Increasing section
for row in range(1, n + 1):

    # Stars on the left
    for _ in range(row):
        print("*", end="")

    # Spaces in the middle
    for _ in range(2 * (n - row)):
        print(" ", end="")

    # Stars on the right
    for _ in range(row):
        print("*", end="")

    print()


# Decreasing section
for row in range(n - 1, 0, -1):

    # Stars on the left
    for _ in range(row):
        print("*", end="")

    # Spaces in the middle
    for _ in range(2 * (n - row)):
        print(" ", end="")

    # Stars on the right
    for _ in range(row):
        print("*", end="")

    print()