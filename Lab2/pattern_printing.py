# This program prints three different patterns using nested loops.


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


n = get_positive_integer("Enter the number of rows: ")


# Pattern 1: Right-angled triangle of stars.
print("\n1. Right-Angled Triangle")

for row in range(1, n + 1):
    for column in range(row):
        print("*", end=" ")
    print()


# Pattern 2: Number pattern.
print("\n2. Number Pattern")

for row in range(1, n + 1):
    for number in range(1, row + 1):
        print(number, end=" ")
    print()


# Pattern 3: Centered pyramid.
print("\n3. Centered Pyramid")

for row in range(1, n + 1):
    for space in range(n - row):
        print(" ", end=" ")

    for star in range(2 * row - 1):
        print("*", end=" ")

    print()