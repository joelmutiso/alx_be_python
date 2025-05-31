size = int(input("Enter the size of the pattern: "))

row = 0

while row < size:
    # Inner loop to print '*' without newline
    for _ in range(size):
        print("*", end="")
    print()  # New line after each row
    row += 1