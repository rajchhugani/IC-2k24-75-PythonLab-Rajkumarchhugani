# Lab 1 - Python Fundamentals

This lab covers the foundational building blocks of Python: variables, data types, operators, user input, string operations, arithmetic calculations, escape sequences, and menu-driven program structures. It is divided into four sections: a concept check, an output prediction exercise, core programs, and an advanced program.

---

## Section A: Quick Concept Check

Short-answer questions to verify understanding of Python basics.

| # | Question | Answer |
|---|----------|--------|
| 1 | `input()` always returns data of type ___ | **`str`** |
| 2 | The function used to check the data type of a variable is ___ | **`type()`** |
| 3 | Convert a string to an integer using ___ function, and to a float using ___ function | **`int()`** and **`float()`** |
| 4 | In Python, `**` is the operator for ___, and `//` is the operator for ___ | **exponentiation** and **floor division** |
| 5 | `%` is called the ___ operator. It gives the ___ | **modulus** operator; gives the **remainder** |
| 6 | A single line comment in Python starts with the symbol ___ | **`#`** |
| 7 | Write one rule for naming a variable (something not allowed) | Variable names **cannot start with a digit** (e.g., `2name` is invalid) |

---

## Section B: Predict the Output

Write your answer before running the code. Run each one after writing, then mark right or wrong.

| # | Expression | Predicted Output | Explanation |
|---|------------|-----------------|-------------|
| 1 | `print(2 + 3 * 4 - 1)` | `13` | `*` has higher precedence → `3*4=12`, then `2+12-1=13` |
| 2 | `print(10 % 3 + 2 ** 2)` | `5` | `**` first → `2**2=4`, then `10%3=1`, then `1+4=5` |
| 3 | `print((5 + 3) / 2 == 4)` | `True` | `8/2=4.0`, and `4.0 == 4` evaluates to `True` |
| 4 | `print(type(5 / 2))` | `<class 'float'>` | `/` always returns a `float` in Python 3 |
| 5 | `print("Python"[1:4])` | `yth` | Slicing from index 1 (inclusive) to 4 (exclusive) |
| 6 | `print("Hi\tThere\nBye")` | `Hi    There` then `Bye` on new line | `\t` inserts a tab; `\n` moves to a new line |

---

## Section C: Core Programs

### 1. Variable and Identifier Practice (`variable_practice.py`)
* **Aim:** Declare variables of different data types and print their values alongside their data types using `type()`.
* **Logic:** Distinct variables are declared to store string, integer, float, and boolean values. Python's built-in `type()` function is invoked within `print()` statements to retrieve and display the explicit data type of each variable.

#### Sample Input / Output:
```text
Name: Raj | Type: <class 'str'>
Age: 20 | Type: <class 'int'>
Height: 5.9 | Type: <class 'float'>
Is Student: True | Type: <class 'bool'>
```

---

### 2. Greeting Program (`greetings.py`)
* **Aim:** Take user inputs for name, age, and city, and output a formatted greeting in a single sentence using an f-string.
* **Logic:** The `input()` function prompts for and reads string inputs for name, age, and city. A formatted string literal (f-string) dynamically interpolates these variable values into a single structured output sentence.

#### Sample Input / Output:
```text
Enter your name: Raj
Enter your age: 20
Enter your city: Indore
Hello, Raj! You are 20 years old and live in Indore.
```

---

### 3. Arithmetic Operations (`arithmetic.py`)
* **Aim:** Calculate and display the sum, difference, product, quotient, and remainder of two numbers provided by the user.
* **Logic:** Raw user inputs are converted to floating-point numbers to accommodate decimal values. Basic arithmetic operators (`+`, `-`, `*`, `/`, `%`) calculate the results, which are printed with clear descriptive labels.

#### Sample Input / Output:
```text
Enter first number: 15
Enter second number: 4
Sum: 19.0
Difference: 11.0
Product: 60.0
Quotient: 3.75
Remainder: 3.0
```

---

### 4. Celsius to Fahrenheit (`celsius_to_fahrenheit.py`)
* **Aim:** Convert a temperature value given in Celsius to Fahrenheit.
* **Logic:** The input temperature is parsed as a floating-point number. The program applies the algebraic formula `(Celsius × 9/5) + 32` to calculate the equivalent Fahrenheit value and prints the formatted result.

#### Sample Input / Output:
```text
Enter temperature in Celsius: 37
37.0°C is equal to 98.6°F
```

---

### 5. String Manipulation (`string_manipulation.py`)
* **Aim:** Perform multiple string operations on a user's full name, including case conversion, reversal, and length calculation.
* **Logic:** Built-in string methods `.upper()` and `.lower()` handle case conversions. Slicing with a negative step `[::-1]` traverses the characters backwards to reverse the string, while `len()` computes the total character count. `.title()` capitalises the first letter of each word.

#### Sample Input / Output:
```text
Enter your full name: Raj Chhugani
Uppercase: RAJ CHHUGANI
Lowercase: raj chhugani
Reversed: inaguhhC jaR
Length of name: 12
Title Case: Raj Chhugani
```

---

### 6. Escape Sequence Practice (`escape_sequence.py`)
* **Aim:** Print a neatly aligned, formatted store receipt using escape sequences.
* **Logic:** Tab escape sequences (`\t`) set fixed horizontal spacing between column headers and item rows, while newline escape sequences (`\n`) format the line breaks across items, dividers, and total amounts. The entire receipt is stored in a single multi-line string using the line-continuation character (`\`).

#### Sample Input / Output:
```text
ITEM            QTY     PRICE
-----------------------------
Coffee          1       4.50
Croissant       2       6.00
Sandwich        1       8.25
-----------------------------
TOTAL                   18.75
```

---

## Section D: Advanced / Optional Program

### 7. Menu-Driven Calculator (`calculator.py`)
* **Aim:** Build a terminal-based calculator supporting at least 4 operations that continuously processes user requests until exit is selected.
* **Logic:** An infinite `while True` loop maintains the menu execution state. User choices trigger conditional branching (`if-elif-else`) to call modular arithmetic functions (`add`, `subtract`, `multiply`, `divide`). Exception handling catches invalid non-numeric entries via `try/except ValueError`, and the `divide()` function explicitly guards against division by zero. Entering option `5` breaks the execution loop.

#### Sample Input / Output:
```text
========== CALCULATOR MENU ==========
1. Addition (+)
2. Subtraction (-)
3. Multiplication (*)
4. Division (/)
5. Exit
Enter your choice (1-5): 1
Enter first number: 12
Enter second number: 8
Result: 12.0 + 8.0 = 20.0

========== CALCULATOR MENU ==========
1. Addition (+)
2. Subtraction (-)
3. Multiplication (*)
4. Division (/)
5. Exit
Enter your choice (1-5): 4
Enter first number: 10
Enter second number: 0
Result: 10.0 / 0.0 = Error! Division by zero is not allowed.

========== CALCULATOR MENU ==========
1. Addition (+)
2. Subtraction (-)
3. Multiplication (*)
4. Division (/)
5. Exit
Enter your choice (1-5): 5
Exiting calculator. Goodbye!
```

---

## File Summary

| File | Section | Description |
|------|---------|-------------|
| `variable_practice.py` | C – Q1 | Declares and prints variables of all basic data types |
| `greetings.py` | C – Q2 | Reads user input and prints a personalised greeting |
| `arithmetic.py` | C – Q3 | Computes and displays five arithmetic operations on two numbers |
| `celsius_to_fahrenheit.py` | C – Q4 | Converts a Celsius temperature to Fahrenheit |
| `string_manipulation.py` | C – Q5 | Applies upper, lower, reverse, length, and title-case on a name |
| `escape_sequence.py` | C – Q6 | Prints a formatted receipt using `\t` and `\n` escape sequences |
| `calculator.py` | D – Q7 | Menu-driven calculator with 4 operations, error handling, and loop |