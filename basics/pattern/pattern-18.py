row=5
for i in range(1,row+1):
    for j in range(i):
        print(chr(69-i+j+1),end='')
    print()
