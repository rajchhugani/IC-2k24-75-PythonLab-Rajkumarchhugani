# Lab 2 - Loops, Number Theory, and Pattern Printing

This lab covers while loops, for loops, recursion, number-theory checks (Armstrong, prime, perfect, palindrome), the Fibonacci series, pattern printing, and a random-number guessing game. All programs validate user input and handle errors gracefully.

---

## 1. Armstrong Number (`armstrong.py`)

**Aim:** Check whether a given number is an Armstrong number, and list all Armstrong numbers within a user-specified range.

**Logic:** An Armstrong number of d digits satisfies the property that the sum of each digit raised to the power d equals the number itself. The digit count is found with `len(str(n))`, then a while loop extracts digits using the modulo operator. For the range search, every number in the range is tested with `is_armstrong()` and collected into a list.

**Sample Input / Output:**

```text
Enter a number to check: 153
153 is an Armstrong number.

Find Armstrong numbers in a range
Enter the starting value: 1
Enter the ending value: 500
Armstrong numbers between 1 and 500:
1 2 3 4 5 6 7 8 9 153 370 371 407
```

---

## 2. Prime Number (`prime.py`)

**Aim:** Check whether a given number is prime, and list all prime numbers up to a user-specified limit.

**Logic:** Numbers less than 2 are immediately rejected. Even numbers greater than 2 are rejected. For the remaining candidates, trial division is performed only up to the square root of the number (while `divisor * divisor <= number`), testing only odd divisors, which significantly reduces the number of checks.

**Sample Input / Output:**

```text
Enter a number to check: 29
29 is a prime number.

Find prime numbers up to a limit
Enter the limit: 50
Prime numbers up to 50:
2 3 5 7 11 13 17 19 23 29 31 37 41 43 47
```

---

## 3. Perfect Number (`perfect_number.py`)

**Aim:** Check whether a given number is a perfect number, and list all perfect numbers up to a user-specified limit.

**Logic:** A perfect number equals the sum of its proper divisors. Divisors are found by iterating up to the square root; when a divisor `d` is found, both `d` and `number // d` are added (unless they are equal, to avoid counting the square root twice). This avoids an O(n) loop over all values below the number.

**Sample Input / Output:**

```text
Enter a number to check: 28
28 is a perfect number.

Find perfect numbers up to a limit
Enter the limit: 1000
Perfect numbers up to 1000:
6 28 496
```

---

## 4. Palindrome (`palindrome.py`)

**Aim:** Check whether a given integer is a numeric palindrome (using digit reversal arithmetic), and check whether a given string is a palindrome (case-insensitive).

**Logic:** For numbers, digits are extracted one by one with `% 10` and assembled into a reversed number using `reversed * 10 + digit`. For strings, the input is lowercased and compared against its slice `[::-1]`. Two separate functions handle the two cases.

**Sample Input / Output:**

```text
Enter a number to check: 12321
12321 is a palindrome.

Enter a string to check: Racecar
"Racecar" is a palindrome.

--- (another run) ---

Enter a number to check: 1234
1234 is not a palindrome.

Enter a string to check: hello
"hello" is not a palindrome.
```

---

## 5. Fibonacci Series (`fibonacci.py`)

**Aim:** Print the first n Fibonacci terms using both an iterative (loop) approach and a recursive approach, and report the total number of recursive function calls made.

**Logic:** The loop version builds the series by swapping `first, second = second, first + second` on each iteration — O(n) time. The recursive version calls `fibonacci_recursive(i)` for each i in 0..n-1; a global counter tracks every call, demonstrating the exponential call overhead of naive recursion.

**Sample Input / Output:**

```text
Enter the number of Fibonacci terms: 8

Fibonacci series using loop:
0 1 1 2 3 5 8 13

Fibonacci series using recursion:
0 1 1 2 3 5 8 13
Number of recursive function calls: 108
```

---

## 6. Pattern Printing (`pattern_printing.py`)

**Aim:** Take a positive integer n and print three patterns in sequence: a right-angled star triangle, a number triangle, and a centered star pyramid.

**Logic:** All three patterns use nested loops with a single validated input n. The right-angled triangle prints `row` stars per row. The number triangle prints numbers 1 through `row`. The centered pyramid uses `n - row` leading spaces and `2 * row - 1` stars to centre each row.

**Sample Input / Output (n = 4):**

```text
1. Right-Angled Triangle
* 
* * 
* * * 
* * * * 

2. Number Pattern
1 
1 2 
1 2 3 
1 2 3 4 

3. Centered Pyramid
      * 
    * * * 
  * * * * * 
* * * * * * * 
```

---

## 7. Number Guessing Game (`number_guessing_game.py`)

**Aim:** The computer picks a random number between 1 and 100; the user has 7 attempts to guess it, receiving "Too low" or "Too high" feedback after each wrong guess.

**Logic:** `random.randint(1, 100)` selects the secret number before the loop. A for loop counts attempts; each guess is validated to lie within 1–100. The function returns immediately on a correct guess, otherwise the loop exhausts all attempts and reveals the secret number.

**Sample Input / Output:**

```text
===== NUMBER GUESSING GAME =====
I have chosen a number between 1 and 100.
You have 7 attempts to guess it.

Attempt 1 of 7
Enter your guess (1-100): 50
Too high!

Attempt 2 of 7
Enter your guess (1-100): 25
Too low!

Attempt 3 of 7
Enter your guess (1-100): 37
Correct! You guessed the number in 3 attempts.
```

---

## 8. Menu-Driven Application (`menu_driven.py`)

**Aim:** Combine all six Lab 2 programs into a single menu-driven application so any feature can be accessed without re-running the script.

**Logic:** A `while True` loop displays the menu and routes to the appropriate function via `if-elif-else`. All helper functions from the individual programs are embedded directly. The Fibonacci recursive option is automatically skipped for n > 20 to prevent excessive computation time. Selecting option 7 breaks the loop and exits.

**Sample Input / Output:**

```text
========== LAB 2 MENU ==========
1. Armstrong Number
2. Prime Number
3. Perfect Number
4. Palindrome
5. Fibonacci Series
6. Pattern Printing
7. Exit
================================
Enter your choice: 5
Enter the number of Fibonacci terms: 6

Fibonacci using loop:
0 1 1 2 3 5

Fibonacci using recursion:
0 1 1 2 3 5

Enter your choice: 7
Exiting the Lab 2 application. Goodbye!
```

---

## File Summary

| File | Description |
|------|-------------|
| `armstrong.py` | Checks a single Armstrong number and lists all in a range |
| `prime.py` | Checks primality and lists all primes up to a limit |
| `perfect_number.py` | Checks a perfect number and lists all up to a limit |
| `palindrome.py` | Checks numeric and string palindromes |
| `fibonacci.py` | Prints Fibonacci series using loop and recursion, counts recursive calls |
| `pattern_printing.py` | Prints right-angled triangle, number triangle, and centered pyramid |
| `number_guessing_game.py` | Random guessing game with 7 attempts and high/low feedback |
| `menu_driven.py` | Combines all above programs into a single menu-driven application |
