n= eval(input("enter the no of row"))
m1=[]
for j in range(n):
    line=input("enter row").strip().split()
    m1.append([eval(x) for x in line])
markv=True
for i in range(n):
    tot=0
    for j in range(n):
        if m1[i][j] >=0:
            tot=tot+m1[j][i]
        else:
            markv=False
            break
    if tot != 1:
        markv=False
if markv==True:
    print("it is a markv")
else:
    print("not a markv")