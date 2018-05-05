# def rev(num):
#     digit=0
#     while num>0:
#         digit=digit*10+num%10
#         num=num//10
#     return digit


def main():
    s=input("enter  the list of integeers sepaarted by space")
    arr=s.split()
    l1=[eval(x) for x in arr ]
    print(l1)
#     for i in range(len(l1)):
#         l1[i]=(rev(l1[i]))
#     print("rev",l1)
    l1.reverse()
    print(l1)
main()