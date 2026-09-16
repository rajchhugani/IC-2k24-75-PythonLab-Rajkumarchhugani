# This program prints a concentric number square pattern.


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


n = get_positive_integer("Enter the number: ")

size = 2 * n - 1

for row in range(size):
    for column in range(size):

        distance_from_edge = min(
            row,
            column,
            size - 1 - row,
            size - 1 - column
        )

        value = n - distance_from_edge

        print(value, end=" ")

    print()