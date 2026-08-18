# Lab 1 - Python Fundamentals

This repository contains basic Python programs covering variables, user input, string operations, arithmetic calculations, formatting, control flow, and menu-driven structures.

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

### 2. Greeting Program (`greeting.py`)
* **Aim:** Take user inputs for name, age, and city, and output a formatted greeting in a single sentence using an f-string.
* **Logic:** The `input()` function prompts for and reads string inputs for name, age, and city. An formatted string literal (f-string) dynamically interpolates these variable values into a single structured output sentence.

#### Sample Input / Output:
```text
Enter your name: Raj
Enter your age: 20
Enter your city: Indore
Hello, Raj! You are 20 years old and live in Indore.
```

---

### 3. Arithmetic Operations (`arithmetic_ops.py`)
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
* **Logic:** The input temperature is parsed as a floating-point number. The program applies the algebraic formula `(Celsius * 9/5) + 32` to calculate the equivalent Fahrenheit value and prints the formatted result.

#### Sample Input / Output:
```text
Enter temperature in Celsius: 37
37.0°C is equal to 98.6°F
```

---

### 5. String Manipulation (`string_manipulation.py`)
* **Aim:** Perform multiple string operations on a user's full name, including case conversion, reversal, and length calculation.
* **Logic:** Built-in string methods `.upper()` and `.lower()` handle case conversions. Slicing with a negative step `[::-1]` traverses the characters backwards to reverse the string, while `len()` computes the total character count.

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

### 6. Escape Sequence Practice (`receipt.py`)
* **Aim:** Print a neatly aligned, formatted store receipt using escape sequences.
* **Logic:** Tab escape sequences (`\t`) set fixed horizontal spacing between column headers and item rows, while newline escape sequences (`\n`) format the line breaks across items, dividers, and total amounts.

#### Sample Input / Output:
```text
Item            Price
--------------------
Coffee          Rs. 100
Croissant       Rs. 150
Sandwich        Rs. 120
--------------------
Total           Rs. 370
```

---

## Section D: Advanced / Optional Program

### 7. Menu-Driven Calculator (`calculator.py`)
* **Aim:** Build a terminal-based calculator supporting at least 4 operations that continuously processes user requests until exit is selected.
* **Logic:** An infinite `while` loop maintains the menu execution state. User choices trigger conditional branching (`if-elif-else`) to call modular arithmetic functions, while exception handling handles invalid non-numeric entries and prevents division by zero. Entering option 5 breaks the execution loop.

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