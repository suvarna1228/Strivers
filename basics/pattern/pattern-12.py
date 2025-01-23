row=4
for i in range(1,row):
    for j in range(1,i+1):
        print(j,end='')
    for j in range(2*(row-i)):
      print(' ', end='')
    for j in range(i, 0, -1):
      print(j, end='')
    print()