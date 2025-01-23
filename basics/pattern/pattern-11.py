row=4
for i in range(1,row+1):
    start=i%2
    for j in range(i):
        print(start,end='')
        start=1-start
    print()
