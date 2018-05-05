n=[]
for i in range(7):
    n.append(eval(input("enter a no")))
# print(n,len(n))
max1=n[0]
for i in range(1,len(n)):
#     print(i," f",n[i])
    if max1 < n[i]:
        max1=n[i]
        count=0
#         print(max1,"max inside",count)
    if max1==n[i]:
        count=count+1
print(max1,"max",count)
    