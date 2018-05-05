# bubble sort
s=input("enter the list")
arr=s.split()
l1=[int(x) for x in arr]
print(l1)
l=len(l1)

for i in range(l):
    for j in range(l):
        if l1[i] < l1[j] :
            temp = l1[i]
            l1[i] = l1[j] 
            l1[j] = temp
print(l1)           