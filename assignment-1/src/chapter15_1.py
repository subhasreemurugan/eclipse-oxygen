def sumDigits(n): 
   print(n)
   if n < 10:
    return n 
   else:
    return n%10 + sumDigits(n//10)
no =eval(input("enter the number"))
sum1=sumDigits(no)
print(sum1,"is the sum")