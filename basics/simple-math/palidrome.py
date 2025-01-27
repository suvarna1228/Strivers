def palidrom(n):
   num=n
   rev=0
   while n>0:
       last=n%10
       n=n//10
       rev=rev*10+last
   if num == rev:
        return "Number is a palindrome"
   else:
        return "Number is not a palindrome"
   
print(palidrom(121))
