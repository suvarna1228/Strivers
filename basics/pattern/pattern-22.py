# Size of the grid
size = 4

# Outer loop for rows
for i in range(size):
    # Inner loop for columns
    for j in range(size):
        # Determine the value to print using nested loops
        for value in range(size, 0, -1):
            if i == value - 1 or j == value - 1 or i == size - value or j == size - value:
                print(value, end=" ")
                break
    print()  # Move to the next row
