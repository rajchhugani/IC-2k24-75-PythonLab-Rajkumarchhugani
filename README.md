# Python Programming Laboratory Repository

**Course:** Python Programming Lab  
**Student Name:** Rajkumar Chhugani  
**Roll / ID:** IC-2k24-75  
**Semester:** 5th Semester  

---

## 📌 Repository Overview

This repository contains all lab assignments, practical exercises, and theoretical analyses completed as part of the Python Programming Laboratory coursework. Each lab is organized into its own dedicated folder containing Python source code (`.py`) and detailed documentation (`README.md`) covering problem statements, logic breakdowns, and verified input/output examples.

---

## 📂 Directory Structure & Lab Summaries

```text
.
├── Lab1/    # Python Fundamentals & Basic Syntax
├── Lab2/    # Loops, Number Theory & Control Flow
├── Lab3/    # Concentric Number & Star Patterns
├── Lab4/    # Advanced Star Patterns (Hollow Diamond & Butterfly)
├── Lab5/    # Matrix Operations & Pattern Printing
├── Lab6/    # Interactive Simulations & Search Algorithms
└── Lab7/    # Algorithmic Complexity (Big-O Time & Space Analysis)
```

---

### [Lab 1: Python Fundamentals](file:///d:/5th%20Sem/IC-2k24-75-PythonLab-Rajkumarchhugani/Lab1/README.md)
Introduction to Python basics, syntax rules, and primitive operations:
- **`variable_practice.py`**: Variable assignment, dynamic typing, and standard naming conventions.
- **`arithmetic.py`**: Arithmetic operators (`+`, `-`, `*`, `/`, `//`, `%`, `**`).
- **`string_manipulation.py`**: String concatenation, indexing, slicing, and string methods.
- **`escape_sequence.py`**: Formatting outputs using escape characters (`\n`, `\t`, quotes).
- **`celsius_to_fahrenheit.py`**: Temperature unit conversion program.
- **`calculator.py`**: Basic interactive arithmetic calculator.
- **`greetings.py`**: User input and personalized greeting formatting.

---

### [Lab 2: Loops, Number Theory & Interactive Programs](file:///d:/5th%20Sem/IC-2k24-75-PythonLab-Rajkumarchhugani/Lab2/README.md)
Implementation of iterative constructs, recursive functions, and mathematical checks:
- **`prime.py`**: Prime number verification with $O(\sqrt{n})$ trial division.
- **`armstrong.py`**: Check for Armstrong (narcissistic) numbers across variable digit lengths.
- **`palindrome.py`**: Numeric and string palindrome verification.
- **`perfect_number.py`**: Proper divisor summation to identify perfect numbers.
- **`fibonacci.py`**: Fibonacci sequence generation (iterative and recursive approaches).
- **`number_guessing_game.py`**: Random number guessing game with feedback (`Too High`/`Too Low`).
- **`menu_driven.py`**: Interactive CLI menu combining multiple utility calculations.
- **`pattern_printing.py`**: Foundational triangle and pyramid star patterns.

---

### [Lab 3: Concentric Number & Star Patterns](file:///d:/5th%20Sem/IC-2k24-75-PythonLab-Rajkumarchhugani/Lab3/README.md)
Advanced nested loop logic for coordinate-based pattern generation:
- **`number_pattern.py`**: Concentric square number pattern of size $(2n - 1) \times (2n - 1)$ using distance-to-edge calculation: $\max(|i - n|, |j - n|) + 1$.
- **`pattern_matching.py`**: Inverted pyramids, mirrored triangles, and composite star layouts.

---

### [Lab 4: Advanced Star Patterns](file:///d:/5th%20Sem/IC-2k24-75-PythonLab-Rajkumarchhugani/Lab4/README.md)
Medium-to-hard geometric star patterns using single unified loops and dynamic spacing:
- **`hollowdiamond.py`**: Hollow diamond pattern for any odd dimension $n$ using `abs(mid - i)` outer spaces and dynamic inner spacing without splitting into hard-coded upper/lower loops.
- **`butterfly.py`**: Symmetric butterfly star pattern with expanding/contracting wings and middle space calculations.

---

### [Lab 5: Star Pattern & Matrix Operations](file:///d:/5th%20Sem/IC-2k24-75-PythonLab-Rajkumarchhugani/Lab5/README.md)
Pattern formatting and raw 2D list matrix manipulation without external libraries:
- **`star_pattern.py`**: Space-separated nested loop star pattern for dynamic $n$.
- **`matrix_operations.py`**: Comprehensive $3 \times 3$ matrix manipulation using native Python lists and loops:
  1. Formatted grid display.
  2. Total matrix element sum.
  3. Main diagonal element sum.
  4. Finding global maximum and minimum values.
  5. Matrix transposition ($A^T$).

---

### [Lab 6: Control Structures, Simulation & Search Algorithms](file:///d:/5th%20Sem/IC-2k24-75-PythonLab-Rajkumarchhugani/Lab6/README.md)
Complex state-tracking, simulations, and algorithmic problem-solving:
- **Section A & B**: Conceptual questions and manual execution trace tables.
- **`atm_simulation.py`**: State-preserving ATM system featuring PIN authorization, deposit, balance check, transaction limits, and overdraw prevention.
- **`computer_guesses.py`**: Binary search algorithm simulation where the computer guesses a user-selected number in $O(\log n)$ attempts.
- **Section E**: List transformations, filtering, and loop analysis.

---

### [Lab 7: Time & Space Complexity Analysis](file:///d:/5th%20Sem/IC-2k24-75-PythonLab-Rajkumarchhugani/Lab7/README.md)
Theoretical and asymptotic analysis using Big-O notation for 22 algorithm snippets:
- Loop bounds and nested iterations ($O(n)$, $O(n^2)$, $O(m \times n)$).
- Logarithmic division and fast exponentiation ($O(\log n)$).
- Divide and conquer vs. naive recursion call stack analysis ($O(2^n)$ vs $O(n)$ stack space).
- Memory footprints of in-place algorithms ($O(1)$) vs slicing and sparse representations ($O(n)$, $O(k)$).

---

## 🛠️ Requirements & How to Run

- **Python Version:** Python 3.8+ (no third-party dependencies required; uses Python standard library only).

### Running Any Script
Navigate into the respective lab folder and execute using `python`:

```bash
# Example: Running Lab 4 Hollow Diamond
cd Lab4
python hollowdiamond.py

# Example: Running Lab 5 Matrix Operations
cd ../Lab5
python matrix_operations.py
```

---

## 👤 Author
- **Rajkumar Chhugani** ([@rajchhugani](https://github.com/rajchhugani))
- Department of Information Technology / Computer Applications
