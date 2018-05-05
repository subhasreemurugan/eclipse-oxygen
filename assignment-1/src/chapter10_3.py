s=input("enter  the list of integeers sepaarted by space")
arr=s.split()
list1=[eval(x) for x in arr ]
print(list1)
# count=0
# while len(list1)>0:
#     count=list1.count(list1[0])
#     if count>1:
#         print(list1[0]," occurs ",count,"times")
#     else:
#         print(list1[0]," occurs ",count,"time")
#     list1.remove(list1[0])
temp=0
counter = 100 * [0]
for i in range(len(list1)):
    temp = list1[i]
    print(temp)
    counter[temp]=list1.count(temp)
for i in range(len(counter)):
    if counter[i]==1:
        print(i,"occcur",counter[i],"time")
    elif counter[i]>=2:
        print(i,"occcur",counter[i],"times")