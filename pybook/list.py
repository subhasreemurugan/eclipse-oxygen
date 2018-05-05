N = int(input())
lst=[]
arr=[]
for i in range(N):
    inp=input()
    lst=inp.split()
    task=lst[0]
    
    if task== 'insert':
        x=int(lst[1])
        y=int(lst[2])
        arr.insert(x,y)
        print(arr,x,y)
    elif task=='print':
        print(arr)
    elif task=='remove':
        arr.remove(int(lst[1]))
    elif task=='append':
        arr.append(int(lst[1]))
    elif task=='sort':
        arr.sort()
    elif task=='pop':
        arr.pop()
    elif task=='reverse':
        arr.reverse()
    i=i+1


# inp=input("enter")
# lst=[]
# lst=inp.split()
# print(lst)
# task=lst[0]
# arr=[]
# if task== 'insert':
#     x=int(lst[1])
#     y=int(lst[2])
#     arr.insert(x,y)
#     print(arr,x,y)






# size=eval(input("size"))
# a=input("array")
# item=a.split()
# lst=[eval(x) for x in item ]
# flst=[]
# print(lst)
# for i in range(size):
#     j=i+1
#     fmax=lst[i]
#     max=lst[i]
#     for j in range(size):
#         max=fmax+lst[j]
#         if fmax>max:
#             max=fmax
#             flst=lst[:j]
#             print("list",flst)
#         j=j+1
#     i=i+1