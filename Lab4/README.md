# Lab 4 - Star Pattern Programs (Medium to Hard)

This lab covers medium-to-hard level star patterns using nested loops and conditional statements. Both programs work for any valid value of n and do not hard-code any output.

---

## Question 1: Hollow Diamond (`hollowdiamond.py`)

**Aim:** Take an odd integer n from the user and print a hollow diamond pattern where only the border stars are printed, not the interior.

**Logic:** The midpoint is computed as `mid = n // 2`. For each row i in 0 to n-1, the number of leading spaces equals `abs(mid - i)`, which decreases towards the middle row and increases back out. The number of inner spaces between the two border stars is `2 * (mid - outer_spaces) - 1`. The top and bottom peaks (where `inner_spaces <= 0`) print only a single star. A single unified loop handles both the upper and lower halves without any separate print sections.

**Sample Output — n = 7:**

```text
   *
  * *
 *   *
*     *
 *   *
  * *
   *
```

**Sample Output — n = 5:**

```text
  *
 * *
*   *
 * *
  *
```

---

## Question 2: Butterfly Pattern (`butterfly.py`)

**Aim:** Take a positive integer n from the user and print a butterfly star pattern with an increasing section (rows 1 to n) followed by a decreasing section (rows n-1 down to 1).

**Logic:** The pattern is divided into two sections sharing the same row formula. For each row, the left side prints `row` stars, the middle prints `2 * (n - row)` spaces, and the right side prints `row` stars again. The increasing section iterates from 1 to n; the decreasing section iterates from n-1 back to 1, creating the mirror effect. Input is validated to ensure n is a positive integer.

**Sample Output — n = 5:**

```text
*        *
**      **
***    ***
****  ****
**********
****  ****
***    ***
**      **
*        *
```

**Sample Output — n = 4:**

```text
*      *
**    **
***  ***
********
***  ***
**    **
*      *
```

---

## File Summary

| File | Question | Description |
|------|---------|-------------|
| `hollowdiamond.py` | Q1 | Prints a hollow diamond for any odd n using a single unified loop |
| `butterfly.py` | Q2 | Prints a butterfly pattern for any positive n using increasing and decreasing sections |
