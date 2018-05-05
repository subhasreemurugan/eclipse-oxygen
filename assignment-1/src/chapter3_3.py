num=eval(input("enter a number to reverse"))
digit=1
rev=0
while num>0:
    digit=num%10
#     print(digit)
    rev=rev*10+digit
#     print(rev)
    num=num//10
print("the reverse of the number is",rev)