
def countLetters(s):
#     print(s,len(s))
    lent=0
    for i in s:
#         print(i)
        if ord(i)>=ord('a') and ord(i)<=ord('z') or ord(i)>=ord('A') and ord(i)<=ord('Z'):
#             print("f",i)
            lent=lent+1
    print("the lenght",lent)
def main():
     
    inp=input("enter the ssntence")
    countLetters(inp)
main()