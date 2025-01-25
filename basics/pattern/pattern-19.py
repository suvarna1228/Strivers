row = 5

# Top part
for i in range(row):
    # Left decreasing stars
    for j in range(row - i):
        print("*", end="")
    # Spaces in the middle
    for j in range(2 * i):
        print(" ", end="")
    # Right decreasing stars
    for j in range(row - i):
        print("*", end="")
    print()

# Bottom part
for i in range(row):
    # Left increasing stars
    for j in range(i + 1):
        print("*", end="")
    # Spaces in the middle
    for j in range(2 * (row - i - 1)):
        print(" ", end="")
    # Right increasing stars
    for j in range(i + 1):
        print("*", end="")
    print()
