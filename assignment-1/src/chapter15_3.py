def gcd(n1,n2):
    if n2!=0:
        return gcd(n2,n1%n2)
    else:
        return n1
n1,n2=eval(input("enter the two number"))
g=gcd(n1,n2)
print("gcd",g)