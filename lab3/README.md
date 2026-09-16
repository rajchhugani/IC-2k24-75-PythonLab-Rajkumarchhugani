# Lab 3 - Concentric Number Pattern and Additional Star Patterns

This lab covers nested loops applied to two pattern-printing tasks: a concentric number square and a collection of additional star and number patterns. Both files work for any valid positive input.

---

## 1. Concentric Number Square (`number_pattern.py`)

**Aim:** Take a positive integer n from the user and print a (2n-1) x (2n-1) concentric number square, where each cell contains the "layer number" counting inward from the border.

**Logic:** The grid size is `2*n - 1`. For every cell at position `(row, column)`, the distance from the nearest edge is `min(row, column, size-1-row, size-1-column)`. The value printed is `n - distance_from_edge`, which equals n at the outer border and decreases to 1 at the centre. A single pair of nested loops handles the entire grid.

**Sample Input / Output (n = 4):**

```text
4 4 4 4 4 4 4
4 3 3 3 3 3 4
4 3 2 2 2 3 4
4 3 2 1 2 3 4
4 3 2 2 2 3 4
4 3 3 3 3 3 4
4 4 4 4 4 4 4
```

**Sample Input / Output (n = 3):**

```text
3 3 3 3 3
3 2 2 2 3
3 2 1 2 3
3 2 2 2 3
3 3 3 3 3
```

---

## 2. Additional Pattern Matching (`pattern_matching.py`)

**Aim:** Demonstrate six different star/number patterns using nested loops and string arithmetic. Each pattern is printed by calling its dedicated function.

**Patterns included:**

| Function | Pattern |
|----------|---------|
| `solid_square(n)` | n x n square of stars |
| `solid_triangle(n)` | Right-angled triangle of stars |
| `equi_triangle(n)` | Centred equilateral-style star triangle |
| `square_triangle(n)` | Hollow-bordered decreasing triangle (stars on edges only) |
| `square_diamond(n)` | Full hollow diamond |
| `hollow_diamond_box(n)` | Hourglass-to-diamond box with solid star borders |

**Logic:** Each function uses string multiplication (`"* " * n`) and concatenation to construct rows, rather than character-by-character inner loops. Leading spaces control alignment. The two-section loop pattern (ascending then descending) is used for symmetric shapes like the diamond and box.

**Sample Output (n = 4 for solid_square, n = 5 for others):**

```text
* * * * 
* * * * 
* * * * 
* * * * 

* *   
* * *   
* * * *   

    *
   ***
  *****
 *******
*********

****  ****
*** **** ***
...

*****     *****
****       ****
...
```

---

## File Summary

| File | Description |
|------|-------------|
| `number_pattern.py` | Prints a concentric number square for any positive n using the min-distance formula |
| `pattern_matching.py` | Prints six different star/number patterns using dedicated functions |
