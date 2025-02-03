def divisors(n):
    list_d=[]
    for i in range(1,n+1):
       if n%i == 0:
           list_d.append(i)

    return list_d

print(divisors(45))
