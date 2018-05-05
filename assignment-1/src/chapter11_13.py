n= eval(input("enter the no of row"))
m1=[]
for j in range(n):
    line=input("enter row").strip().split()
    m1.append([eval(x) for x in line])
larg = m1[0][0]
for i in range(n):
    for j in range(n):
        if m1[i][j] > larg:
            larg=m1[i][j]
            x=i
            y=j
print ("The location of the largest element is at (",x,",",y,")")