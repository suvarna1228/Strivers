# Dimensions of the rectangle
rows = 5
columns = 6

for i in range(rows):
    for j in range(columns):
        # Print '*' for borders
        if i == 0 or i == rows - 1 or j == 0 or j == columns - 1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()  # Move to the next row
