s=input("enter the list")
arr=s.split()
l1=[x for x in arr]
flag=True
for i in range(1,len(l1)):
#     if not int then 9 becomes greater then 10
    if int(l1[i-1]) > int(l1[i]):
#         print(l1[i-1],"fgdgf",l1[i]," ",l1[i-1]>l1[i])
        flag=False
        break
if flag==True:
    print(" sorted")
else:
    print("not sorted")
print(9>10)
