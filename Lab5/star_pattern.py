# This program prints a right-angled star pattern.
# The user can enter any positive number of rows.


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


for row in range(1, n + 1):
    for column in range(row):
        print("*", end=" ")
    print()