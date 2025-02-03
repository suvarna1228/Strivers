def isprime(n):
    list_d=[]
    for i in range(1,n+1):
       if n%i == 0:
           list_d.append(i)

    if len(list_d)>2:
        print("not prime number")
    else:
        print("it  is  prime")
print(isprime(5))
print(isprime(9))