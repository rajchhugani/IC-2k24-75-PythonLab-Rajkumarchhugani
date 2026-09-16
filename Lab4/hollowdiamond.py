n = int(input("Enter an odd number: "))

if n % 2 == 0:
    print("Please enter an odd number.")
else:
    mid = n // 2

    for i in range(n):
        # Outer spaces decrease toward the middle, then increase
        outer_spaces = abs(mid - i)
        
        # Inner spaces between stars: 2 * (mid - outer_spaces) - 1
        inner_spaces = 2 * (mid - outer_spaces) - 1

        # 1. Print leading spaces
        for _ in range(outer_spaces):
            print(" ", end="")

        # 2. Print first star
        print("*", end="")

        # 3. Print inner spaces and second star (if not top/bottom peak)
        if inner_spaces > 0:
            for _ in range(inner_spaces):
                print(" ", end="")
            print("*", end="")

        print()