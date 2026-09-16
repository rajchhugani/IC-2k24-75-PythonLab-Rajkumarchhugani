# Lab 7 - Algorithm Complexity Analysis

This lab contains no programs to write. For each code snippet below, the time and space complexities are stated using Big-O notation with a one-line justification.

---

## Snippet 1 — `find_max`

```python
def find_max(arr):
    max_val = arr[0]
    for i in range(1, len(arr)):
        if arr[i] > max_val:
            max_val = arr[i]
    return max_val
```

| | Complexity |
|-|-----------|
| **Time** | O(n) |
| **Space** | O(1) |

**Justify:** The loop visits every element exactly once, and only a single extra variable (`max_val`) is kept regardless of input size.

---

## Snippet 2 — `has_duplicate`

```python
def has_duplicate(arr):
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] == arr[j]:
                return True
    return False
```

| | Complexity |
|-|-----------|
| **Time** | O(n²) |
| **Space** | O(1) |

**Justify:** Every pair of elements is compared in a nested loop (n*(n-1)/2 comparisons), and no extra data structure is allocated.

---

## Snippet 3 — `sum_digits`

```python
def sum_digits(n):
    if n == 0:
        return 0
    return n % 10 + sum_digits(n // 10)
```

| | Complexity |
|-|-----------|
| **Time** | O(d) where d = number of digits in n |
| **Space** | O(d) |

**Justify:** The function recurses once per digit (floor-dividing by 10 each time), and each call frame stays on the stack until the base case is reached.

---

## Snippet 4 — `print_pairs`

```python
def print_pairs(arr):
    n = len(arr)
    result = []
    for i in range(n):
        for j in range(n):
            result.append((arr[i], arr[j]))
    return result
```

| | Complexity |
|-|-----------|
| **Time** | O(n²) |
| **Space** | O(n²) |

**Justify:** The nested loop generates every ordered pair — n² iterations — and all n² tuples are stored in `result`, so both dimensions are quadratic.

---

## Snippet 5 — `binary_search`

```python
def binary_search(arr, target):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1
```

| | Complexity |
|-|-----------|
| **Time** | O(log n) |
| **Space** | O(1) |

**Justify:** Each iteration halves the search interval, so at most log₂(n) iterations are needed, and only a fixed number of pointer variables are used.

---

## Snippet 6 — `matrix_multiply`

```python
def matrix_multiply(a, b):
    n = len(a)
    result = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                result[i][j] += a[i][k] * b[k][j]
    return result
```

| | Complexity |
|-|-----------|
| **Time** | O(n³) |
| **Space** | O(n²) |

**Justify:** Three nested loops each run n times giving n³ multiply-add operations, and the output matrix `result` occupies n² cells.

---

## Snippet 7 — `to_sparse`

```python
def to_sparse(matrix):
    triples = []
    for r in range(len(matrix)):
        for c in range(len(matrix[0])):
            if matrix[r][c] != 0:
                triples.append((r, c, matrix[r][c]))
    return triples
```

| | Complexity |
|-|-----------|
| **Time** | O(m × n) |
| **Space** | O(k) — where k is the number of non-zero elements |

**Justify:** Every cell of the m×n matrix is visited exactly once to check if it is non-zero; only the k non-zero entries are stored in `triples`.

---

## Snippet 8 — `process`

```python
def process(arr):
    n = len(arr)
    for i in range(n):
        print(arr[i])
    for j in range(n):
        for k in range(n):
            print(arr[j], arr[k])
```

| | Complexity |
|-|-----------|
| **Time** | O(n²) |

**Justify:** The single loop runs in O(n) and the nested loop runs in O(n²); since O(n²) dominates O(n), the overall complexity is O(n²).

---

## Snippet 9 — `check_first_ten`

```python
def check_first_ten(arr):
    for i in range(len(arr)):
        for j in range(10):
            if arr[i] == j:
                return True
    return False
```

| | Complexity |
|-|-----------|
| **Time** | O(n) |

**Justify:** The inner loop always runs exactly 10 times (a constant), so the total work is 10n, which simplifies to O(n).

---

## Snippet 10 — `reverse_new`

```python
def reverse_new(arr):
    reversed_arr = []
    for i in range(len(arr) - 1, -1, -1):
        reversed_arr.append(arr[i])
    return reversed_arr
```

| | Complexity |
|-|-----------|
| **Time** | O(n) |
| **Space** | O(n) |

**Justify:** Every element is appended once to a new list of size n, so both time and space scale linearly with input size.

---

## Snippet 11 — `reverse_in_place`

```python
def reverse_in_place(arr):
    left, right = 0, len(arr) - 1
    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1
    return arr
```

| | Complexity |
|-|-----------|
| **Time** | O(n) |
| **Space** | O(1) |

**Justify:** The two pointers meet in the middle after n/2 swaps done in-place; no extra array is allocated.

---

## Snippet 12 — `factorial`

```python
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)
```

| | Complexity |
|-|-----------|
| **Time** | O(n) |
| **Space** | O(n) |

**Justify:** The function makes n recursive calls, one per decrement; each call frame remains on the call stack until the base case is reached, giving O(n) stack depth.

---

## Snippet 13 — `fibonacci`

```python
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)
```

| | Complexity |
|-|-----------|
| **Time** | O(2ⁿ) |
| **Space** | O(n) |

**Justify:** Each call branches into two more calls with no memoisation, forming a binary tree of ~2ⁿ nodes; the maximum call stack depth at any point is only n (the longest path from root to leaf).

---

## Snippet 14 — `count_pairs_with_sum`

```python
def count_pairs_with_sum(arr, target):
    seen = set()
    count = 0
    for num in arr:
        if target - num in seen:
            count += 1
        seen.add(num)
    return count
```

| | Complexity |
|-|-----------|
| **Time** | O(n) |
| **Space** | O(n) |

**Justify:** Each element is processed once with O(1) average-case set lookup and insertion; the `seen` set can grow to at most n elements.

---

## Snippet 15 — `print_all_subsets`

```python
def print_all_subsets(arr):
    n = len(arr)
    for i in range(2 ** n):
        subset = []
        for j in range(n):
            if i & (1 << j):
                subset.append(arr[j])
        print(subset)
```

| | Complexity |
|-|-----------|
| **Time** | O(n × 2ⁿ) |

**Justify:** There are 2ⁿ subsets, and constructing each one requires checking all n bits, giving n × 2ⁿ total operations.

---

## Snippet 16 — `merge_sorted`

```python
def merge_sorted(a, b):
    result = []
    i = j = 0
    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            result.append(a[i])
            i += 1
        else:
            result.append(b[j])
            j += 1
    result.extend(a[i:])
    result.extend(b[j:])
    return result
```

Let m = len(a), n = len(b).

| | Complexity |
|-|-----------|
| **Time** | O(m + n) |
| **Space** | O(m + n) |

**Justify:** Every element from both arrays is appended exactly once to `result`; the output list holds all m + n elements.

---

## Snippet 17 — `is_palindrome`

```python
def is_palindrome(s):
    return s == s[::-1]
```

| | Complexity |
|-|-----------|
| **Time** | O(n) |
| **Space** | O(n) |

**Justify:** Slicing `s[::-1]` creates a new reversed copy of the string in O(n) time and O(n) space, then the equality check scans both strings in O(n).

---

## Snippet 18 — `flatten`

```python
def flatten(matrix):
    flat = []
    for row in matrix:
        for val in row:
            flat.append(val)
    return flat
```

Let the matrix have m rows and n columns.

| | Complexity |
|-|-----------|
| **Time** | O(m × n) |
| **Space** | O(m × n) |

**Justify:** Every one of the m × n cells is visited once and appended to `flat`, which ultimately holds all m × n values.

---

## Snippet 19 — `power`

```python
def power(base, exp):
    if exp == 0:
        return 1
    return base * power(base, exp - 1)
```

| | Complexity |
|-|-----------|
| **Time** | O(exp) |
| **Space** | O(exp) |

**Justify:** The function decrements `exp` by 1 on each call, making exactly exp recursive calls; each frame sits on the stack until the base case, so stack depth equals exp.

---

## Snippet 20 — `fast_power`

```python
def fast_power(base, exp):
    if exp == 0:
        return 1
    half = fast_power(base, exp // 2)
    if exp % 2 == 0:
        return half * half
    return half * half * base
```

| | Complexity |
|-|-----------|
| **Time** | O(log exp) |
| **Space** | O(log exp) |

**Justify:** The exponent is halved on every recursive call (exponentiation by squaring), so the recursion depth is log₂(exp); each level uses O(1) extra space beyond the call frame.

---

## Snippet 21 — `has_common_element`

```python
def has_common_element(a, b):
    for x in a:
        for y in b:
            if x == y:
                return True
    return False
```

Let p = len(a), q = len(b).

| | Complexity |
|-|-----------|
| **Time** | O(p × q) |
| **Space** | O(1) |

**Justify:** In the worst case every element of `a` is compared against every element of `b`; no extra data structure is allocated.

---

## Snippet 22 — `build_frequency_map`

```python
def build_frequency_map(arr):
    freq = {}
    for val in arr:
        freq[val] = freq.get(val, 0) + 1
    return freq
```

| | Complexity |
|-|-----------|
| **Time** | O(n) |
| **Space** | O(n) |

**Justify:** Each element is processed once with O(1) average-case dictionary operations; in the worst case (all unique values) the dictionary stores n entries.

---

## Quick Reference Table

| # | Function | Time | Space |
|---|----------|------|-------|
| 1 | `find_max` | O(n) | O(1) |
| 2 | `has_duplicate` | O(n²) | O(1) |
| 3 | `sum_digits` | O(d) | O(d) |
| 4 | `print_pairs` | O(n²) | O(n²) |
| 5 | `binary_search` | O(log n) | O(1) |
| 6 | `matrix_multiply` | O(n³) | O(n²) |
| 7 | `to_sparse` | O(m×n) | O(k) |
| 8 | `process` | O(n²) | — |
| 9 | `check_first_ten` | O(n) | — |
| 10 | `reverse_new` | O(n) | O(n) |
| 11 | `reverse_in_place` | O(n) | O(1) |
| 12 | `factorial` | O(n) | O(n) |
| 13 | `fibonacci` | O(2ⁿ) | O(n) |
| 14 | `count_pairs_with_sum` | O(n) | O(n) |
| 15 | `print_all_subsets` | O(n·2ⁿ) | — |
| 16 | `merge_sorted` | O(m+n) | O(m+n) |
| 17 | `is_palindrome` | O(n) | O(n) |
| 18 | `flatten` | O(m×n) | O(m×n) |
| 19 | `power` | O(exp) | O(exp) |
| 20 | `fast_power` | O(log exp) | O(log exp) |
| 21 | `has_common_element` | O(p×q) | O(1) |
| 22 | `build_frequency_map` | O(n) | O(n) |
