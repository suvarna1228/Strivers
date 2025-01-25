row=4
for i in range(1,row):
    for j in range(i):
        print("*",end='')
    
    for j in range(2 * (row - i)):
        print(" ", end="")

    for j in range(i):
        print("*",end='')
    print()

for i in range(row, 0, -1):
    # Left triangle
    for j in range(i):
        print("*", end="")
    # Spaces between the triangles
    for j in range(2 * (row - i)):
        print(" ", end="")
    # Right triangle
    for j in range(i):
        print("*", end="")
    print()