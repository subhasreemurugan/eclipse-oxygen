def sumdig(num):
    sum1=0
    while(num >0):
        sum1=sum1+num%10
        num=num//10
    print(sum1,"the total")
num=eval(input("enter a number"))
sumdig(num)