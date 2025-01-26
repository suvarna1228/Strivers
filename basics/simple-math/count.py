def countDigit(n):
   count=0
   while n>0:
      last=n%10
      n=n//10
      count += 1
   return count
print(countDigit(12345))

