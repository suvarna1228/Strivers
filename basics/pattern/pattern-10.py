row=4
for i in range(1,row+1):
    for j in range(i):
        print("*",end='')
    print()
for i in range(row):
    for j in range(row-i):
        print("*",end='')
    print()
