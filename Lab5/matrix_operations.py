# This program performs operations on a 3 x 3 matrix.
# It displays the matrix, calculates sums, finds the
# largest and smallest elements, and displays the transpose.


def get_integer(prompt):
    """Take and validate an integer from the user."""

    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input. Please enter an integer.")


def input_matrix():
    """Take a 3 x 3 matrix from the user."""

    matrix = []

    print("Enter the elements of the 3 x 3 matrix:")

    for row in range(3):
        current_row = []

        for column in range(3):
            value = get_integer(
                f"Enter element [{row + 1}][{column + 1}]: "
            )
            current_row.append(value)

        matrix.append(current_row)

    return matrix


def display_matrix(matrix):
    """Display the matrix row by row."""

    for row in matrix:
        for element in row:
            print(element, end=" ")
        print()


def sum_of_elements(matrix):
    """Calculate the sum of all matrix elements."""

    total = 0

    for row in matrix:
        for element in row:
            total += element

    return total


def diagonal_sum(matrix):
    """Calculate the sum of the main diagonal."""

    total = 0

    for i in range(3):
        total += matrix[i][i]

    return total


def find_largest(matrix):
    """Find the largest element in the matrix."""

    largest = matrix[0][0]

    for row in matrix:
        for element in row:
            if element > largest:
                largest = element

    return largest


def find_smallest(matrix):
    """Find the smallest element in the matrix."""

    smallest = matrix[0][0]

    for row in matrix:
        for element in row:
            if element < smallest:
                smallest = element

    return smallest


def transpose_matrix(matrix):
    """Create and return the transpose of the matrix."""

    transpose = []

    for column in range(3):
        new_row = []

        for row in range(3):
            new_row.append(matrix[row][column])

        transpose.append(new_row)

    return transpose


# Take matrix input.
matrix = input_matrix()

# Display the original matrix.
print("\nOriginal Matrix:")
display_matrix(matrix)

# Calculate and display the sum of all elements.
print("\nSum of all elements:", sum_of_elements(matrix))

# Calculate and display the main diagonal sum.
print("Sum of main diagonal elements:", diagonal_sum(matrix))

# Find and display largest and smallest elements.
print("Largest element:", find_largest(matrix))
print("Smallest element:", find_smallest(matrix))

# Display the transpose.
print("\nTranspose of the Matrix:")
display_matrix(transpose_matrix(matrix))