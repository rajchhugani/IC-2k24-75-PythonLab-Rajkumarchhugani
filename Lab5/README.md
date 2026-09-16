# Lab 5 - Star Pattern and Matrix Operations

This lab covers nested loops for pattern printing and list-based matrix operations. It contains two programs written without any external libraries.

---

## Question 1: Star Pattern (`star_pattern.py`)

**Aim:** Take a positive integer n from the user and print a right-angled triangle star pattern using nested loops.

**Logic:** An outer loop iterates from 1 to n (inclusive), representing each row. An inner loop runs exactly as many times as the current row number, printing a star followed by a space on each iteration. A `print()` call after the inner loop moves to the next line. Input is validated to ensure n is a positive integer.

**Sample Input / Output:**

```text
Enter the number of rows: 5
* 
* * 
* * * 
* * * * 
* * * * * 
```

Invalid input case:
```text
Enter the number of rows: -3
Please enter a positive integer.
Enter the number of rows: abc
Invalid input. Please enter an integer.
Enter the number of rows: 3
* 
* * 
* * * 
```

---

## Question 2: Matrix Operations (`matrix_operations.py`)

**Aim:** Input a 3×3 matrix from the user and perform five operations: display the matrix, compute the sum of all elements, compute the main diagonal sum, find the largest and smallest elements, and display the transpose.

**Logic:** The matrix is stored as a list of lists. Each element is read individually with validation via `try/except`. Separate functions handle each operation — `sum_of_elements` and `diagonal_sum` use nested loops and index-based access respectively, `find_largest`/`find_smallest` track a running extreme value, and `transpose_matrix` builds a new matrix by swapping row and column indices. No NumPy is used.

**Sample Input / Output:**

```text
Enter the elements of the 3 x 3 matrix:
Enter element [1][1]: 1
Enter element [1][2]: 2
Enter element [1][3]: 3
Enter element [2][1]: 4
Enter element [2][2]: 5
Enter element [2][3]: 6
Enter element [3][1]: 7
Enter element [3][2]: 8
Enter element [3][3]: 9

Original Matrix:
1 2 3 
4 5 6 
7 8 9 

Sum of all elements: 45
Sum of main diagonal elements: 15
Largest element: 9
Smallest element: 1

Transpose of the Matrix:
1 4 7 
2 5 8 
3 6 9 
```

Invalid input case:
```text
Enter element [1][1]: abc
Invalid input. Please enter an integer.
Enter element [1][1]: 5
```

---

## File Summary

| File | Question | Description |
|------|---------|-------------|
| `star_pattern.py` | Q1 | Prints a right-angled star triangle for any positive n using nested loops |
| `matrix_operations.py` | Q2 | Inputs a 3×3 matrix and performs display, sum, diagonal sum, min/max, and transpose operations |
