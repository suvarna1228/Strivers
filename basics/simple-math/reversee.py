def reversenum(n):
   rev=0
   while n>0:
       last=n%10
       n=n//10
       rev=rev*10+last
   return rev
   
print(reversenum(12345))

