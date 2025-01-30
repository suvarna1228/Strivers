def amstrong(n):
    num=n
    sum=0
    while n>0:
      last=n%10
      n=n//10
      sum=sum+last*last*last
    if num == sum:
        return "Number is a palindrome"
    else:
        return "Number is not a palindrome"
   
print(amstrong(121))
print(amstrong(153))