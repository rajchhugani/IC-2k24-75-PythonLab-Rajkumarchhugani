# Lab 6 - Menu-Driven Programs and Games

This lab covers menu-driven programs, random number generation, binary search logic, input validation, and modular program design. It is divided into five sections: a concept check, a trace-the-logic exercise, core programs, analysis questions, and documentation.

---

# Section A: Concept Check

| # | Question | Answer |
|---|----------|--------|
| 1 | When a menu-driven program needs to remember something across multiple choices in the same run, that value must be stored ___ the main loop, not inside it | **outside** |
| 2 | To generate a random number in Python, you first need to ___ the random module | **import** |
| 3 | In a "computer guesses your number" game, the computer narrows its guesses using feedback from the user, which is the same principle as a ___ search | **binary** |
| 4 | If a withdrawal amount in an ATM simulation exceeds the current balance, the correct response is to ___ the transaction and print an error | **reject** |
| 5 | A while loop condition that depends on a variable changed inside the loop will only terminate if that variable is ___ correctly on every iteration | **updated** |

---

# Section B: Trace the Logic

## 1. ATM Simulation

Starting balance: **Rs. 5000**

| Step | Operation | Amount | Balance After | Notes |
|------|-----------|--------|--------------|-------|
| 1 | Check Balance | - | Rs. 5000 | No change |
| 2 | Withdraw | Rs. 2000 | Rs. 3000 | Approved |
| 3 | Deposit | Rs. 500 | Rs. 3500 | Approved |
| 4 | Withdraw | Rs. 4000 | Rs. 3500 | **Rejected** - amount (Rs. 4000) exceeds balance (Rs. 3500) |

**Final Balance: Rs. 3500**

The Rs. 4000 withdrawal is rejected because the current balance is only Rs. 3500. Allowing it would result in a negative balance, which must never happen.

---

## 2. Reverse Guessing Game

Secret number: **37** / Range: **1-100** / Strategy: always guess the midpoint

| Guess # | Current Range | Midpoint Guess | User Feedback | New Range |
|---------|--------------|---------------|--------------|-----------|
| 1 | 1-100 | 50 | Too high | 1-49 |
| 2 | 1-49 | 25 | Too low | 26-49 |
| 3 | 26-49 | 37 | Correct! | - |

```text
Guess 1: 50  ->  Too High   (new range: 1-49)
Guess 2: 25  ->  Too Low    (new range: 26-49)
Guess 3: 37  ->  Correct!
```

The computer found the number in **3 guesses**.

---

## 3. Student Grade Calculator

Marks entered: **85, 92, 78, 60, 55**

```
Average = (85 + 92 + 78 + 60 + 55) / 5
        = 370 / 5
        = 74.0
```

| Subject | Marks |
|---------|-------|
| Subject 1 | 85 |
| Subject 2 | 92 |
| Subject 3 | 78 |
| Subject 4 | 60 |
| Subject 5 | 55 |
| **Average** | **74.0** |
| **Grade** | **C** (60-74 range) |

---

# Section C: Programs to Write

All programs are implemented as separate `.py` files in this folder. Each uses functions and handles invalid input without crashing.

| # | File | Description |
|---|------|-------------|
| 1 | `atm_simulation.py` | Menu-driven ATM with PIN authentication and balance protection |
| 2 | `grade_calculator.py` | Menu-driven student grade calculator with persistent last-student storage |
| 3 | `reverse_guessing.py` | Computer guesses the user's number via binary search |
| 4 | `guessing_game_hints.py` | User guesses a random number with even/odd and multiple-of-5 hints, plus scoring |
| 5 | `combined_application.py` | Top-level menu combining programs 1, 2, and 4 |

---

# Section D: Analysis

### 1. Why binary search guarantees far fewer guesses (Reverse Guessing Game)

With a linear (one-by-one) search in a range of 1-100, the computer might need up to **100 guesses** in the worst case. Binary search halves the remaining search space with every single guess. After 1 guess the range shrinks to at most 50 numbers; after 2 guesses to at most 25; after k guesses to at most 100 / 2^k. This means the computer is guaranteed to find any number within at most **ceil(log2(100)) = 7 guesses**, regardless of what number the user picks. For a range of 1-100, that is roughly 14 times faster in the worst case compared to a linear search.

---

### 2. What goes wrong if the balance check happens after subtraction (ATM)

If the code subtracts the withdrawal amount from the balance first and checks whether the result is valid afterwards, the balance temporarily holds a negative value. Even if the program catches this and tries to restore the original balance, any crash, uncaught exception, or missed code path between the subtraction and the check would leave the account permanently in a negative state. The correct approach is to check `amount <= balance` *before* touching the balance variable at all, so the account is never modified unless the transaction is already known to be valid.

---

### 3. Do the even/odd and multiple-of-5 hints make the game easier?

Yes, significantly. In a plain guessing game with a range of 1-100 and no information, a player using binary search needs about **7 guesses** on average. The even/odd hint alone immediately eliminates 50 candidates: if the secret number is odd, all 50 even numbers can be ignored. The multiple-of-5 hint further narrows the set; only 20 numbers in 1-100 are multiples of 5, and combining both hints the player knows the secret belongs to a group of just 10 numbers. This reduces the effective search space from 100 down to roughly 40 after just the first wrong guess, which can cut the expected number of guesses from 7 down to **3-4** for a well-informed player.

---

### 4. What had to change to allow returning to the top-level menu (Combined Application)

In each individual program, the "exit" option either called `sys.exit()` or relied on the script ending naturally. To embed them inside `combined_application.py`, two things were changed:

- **All program logic was wrapped in a function.** `atm_application()`, `grade_application()`, and `guessing_game()` each contain their own inner `while` loop. The top-level `main()` can call the function, and when it returns the outer menu loop continues.
- **Every internal "Exit" branch uses `return` instead of `sys.exit()`.** `return` exits only that function and hands control back to the caller (`main()`), whereas `sys.exit()` would terminate the entire Python process. This single change allows each sub-program to act as a module that can be entered and exited repeatedly without ending the whole session.

---

# Section E: Documentation

## 1. ATM Simulation (`atm_simulation.py`)

**Aim:** Simulate a menu-driven ATM that lets a user check their balance, deposit money, withdraw money, and change their PIN, with PIN authentication required at entry.

**Logic:** The balance and PIN are initialised as constants before the loop. The program first prompts for the PIN and denies access on a mismatch. Inside the `while True` loop each menu option is handled by a conditional branch. Withdrawals validate `amount <= balance` before modifying state, so the balance can never become negative. The loop continues until the user selects Exit.

**Sample Input / Output:**

```text
Enter your PIN: 0000
Incorrect PIN. Access denied.

--- (re-run) ---

Enter your PIN: 1234
PIN accepted. Welcome!

===== ATM MENU =====
1. Check Balance
2. Deposit
3. Withdraw
4. Change PIN
5. Exit
Enter your choice: 3
Enter withdrawal amount: 6000
Transaction rejected.
Insufficient balance.

Enter your choice: 2
Enter deposit amount: -200
Amount cannot be negative.

Enter your choice: 1
Current balance: Rs. 5000.00

Enter your choice: 5
Exiting ATM...
```

---

## 2. Student Grade Calculator (`grade_calculator.py`)

**Aim:** Take marks for 5 subjects, compute the average, assign a letter grade, and let the user view the last entered student's result from a menu at any time.

**Logic:** `last_student` is initialised as `None` before the `while True` loop so its value persists across menu iterations. Each mark is validated in the range 0-100 with a `try/except` loop. The `calculate_grade()` helper maps the average to A/B/C/D/F using `if-elif-else`. Option 2 displays the stored dictionary and guards against the case where no data has been entered yet.

**Sample Input / Output:**

```text
===== STUDENT GRADE CALCULATOR =====
1. Enter marks for a new student
2. View grade of last entered student
3. Exit
Enter your choice: 2
No student data has been entered yet.

Enter your choice: 1
Enter marks for subject 1: 85
Enter marks for subject 2: 92
Enter marks for subject 3: 78
Enter marks for subject 4: 60
Enter marks for subject 5: 55

Student data saved successfully.
Average: 74.00
Grade: C

Enter your choice: 2
===== LAST ENTERED STUDENT =====
Marks: 85.0 92.0 78.0 60.0 55.0
Average: 74.00
Grade: C
```

---

## 3. Reverse Guessing Game (`reverse_guessing.py`)

**Aim:** The user secretly thinks of a number within a range they specify; the computer finds it using a binary-search strategy, then reports how many guesses it took.

**Logic:** The user provides lower and upper bounds which the computer validates. Inside a `while lower <= upper` loop, the computer calculates `(lower + upper) // 2` as its guess. The user gives feedback (`h`, `l`, or `c`); on `h` the upper bound shrinks to `guess - 1` and on `l` the lower bound grows to `guess + 1`. The loop terminates on correct feedback or collapses if the range becomes impossible (inconsistent feedback).

**Sample Input / Output:**

```text
===== REVERSE GUESSING GAME =====
Enter the lower limit: 1
Enter the upper limit: 100

Think of a number between 1 and 100.
I will try to guess it using binary search.

My guess is: 50
Enter feedback (h = too high, l = too low, c = correct): h

My guess is: 25
Enter feedback (h = too high, l = too low, c = correct): l

My guess is: 37
Enter feedback (h = too high, l = too low, c = correct): c
I guessed your number in 3 guesses!
```

---

## 4. Guessing Game with Hints and Scoring (`guessing_game_hints.py`)

**Aim:** The computer picks a random number in 1-100; the user has 7 attempts to guess it. After each wrong guess, hints reveal whether the secret number is even/odd and a multiple of 5. The user starts with 100 points and loses 10 per wrong guess; a score of 0 is given if all attempts are used.

**Logic:** `random.randint(1, 100)` selects the secret before the loop. A `for` loop counts attempts up to the maximum. Each wrong guess decrements the score by 10 and prints two hints calculated with the `%` operator. If the guess is correct, the final score is shown and the function returns. If all attempts are exhausted the program prints "You lost!" with a score of 0.

**Sample Input / Output:**

```text
===== GUESSING GAME WITH HINTS =====
I selected a number between 1 and 100.
You have 7 attempts.
You start with 100 points.
Each wrong guess costs 10 points.

Attempt 1 of 7
Enter your guess (1-100): 50
Too high!
Hint: The secret number is odd.
Hint: The secret number is not a multiple of 5.

Attempt 2 of 7
Enter your guess (1-100): 25
Too low!
Hint: The secret number is odd.
Hint: The secret number is not a multiple of 5.

Attempt 3 of 7
Enter your guess (1-100): 37

Correct!
You guessed the number in 3 attempts.
Final score: 80
```

---

## 5. Combined Application (`combined_application.py`)

**Aim:** Provide a single entry point with a top-level menu that lets the user choose between the ATM, the Grade Calculator, and the Guessing Game, returning to this menu after exiting any sub-program.

**Logic:** Each sub-program is encapsulated in its own function (`atm_application`, `grade_application`, `guessing_game`). The top-level `main()` runs a `while True` loop that prints the main menu and calls the appropriate function based on the user's choice. Each sub-program's internal "Exit" option uses `return` so control flows back to `main()` rather than ending the process. Selecting option 4 at the top level breaks the outer loop and terminates the program.

**Sample Input / Output:**

```text
================================
       COMBINED APPLICATION
================================
1. ATM
2. Grade Calculator
3. Guessing Game
4. Exit
================================
Enter your choice: 2

===== GRADE CALCULATOR =====
1. Enter marks for a new student
2. View grade of last entered student
3. Exit
Enter your choice: 3
Exiting Grade Calculator...

================================
       COMBINED APPLICATION
================================
1. ATM
2. Grade Calculator
3. Guessing Game
4. Exit
================================
Enter your choice: 4
Exiting Combined Application. Goodbye!
```
