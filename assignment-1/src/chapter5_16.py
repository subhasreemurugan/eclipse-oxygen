n1,n2=eval(input("enter 2 no n1,n2"))


if n1<n2:
    d=n1
else:
    d=n2
for i in range(d,1,-1):
    if n1%d==0 and n2%d==0:
        print("gcd=",d)
