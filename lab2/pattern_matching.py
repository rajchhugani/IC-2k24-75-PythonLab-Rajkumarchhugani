def solid_square(n):
    for i in range(n):
        print("* " * n)
solid_square(4)
print()

def solid_triangle(n):
    for i in range(1, n + 1):
            print("* " * i + "  " * (n - i) )
solid_triangle(4)
print()

def equi_triangle(n):
    for i in range(1, n + 1):
        print(" " * (n - i) + "*" * (2 * i - 1))
equi_triangle(5)
print()

def square_triangle(n):
    for i in range(1, n + 1):
        print("*" * (n - i) + " " * (2 * i - 1) + "*" * (n - i))
square_triangle(5)
print()

def square_diamond(n):
    for i in range(1, n + 1):
        print("*" * (n - i) + " " * (2 * i - 1) + "*" * (n - i))
    for i in range(n-2,-1,-1):
        print("*" * (n - i) + " " * (2 * i - 1) + "*" * (n - i))   
square_diamond(5)
print()

def hollow_diamond_box(n):
    for i in range(n):
        stars = "*" * (n - i)
        spaces = " " * (2 * i)
        print(stars + spaces + stars)

    for i in range(n - 2, -1, -1):
        stars = "*" * (n - i)
        spaces = " " * (2 * i)
        print(stars + spaces + stars)
hollow_diamond_box(5)








    