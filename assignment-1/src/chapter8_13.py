def prefix(str1,str2):
    if len(str1)>len(str2):
        l=len(str2)
    else:
        l=len(str1)
    count=0
    for i in range(l):
        if str1[i]==str2[i]:
#             print(str1[i])
            count=count+1
        else:
            break
    return count
def main():
    str1=input("enter the first string")
    str2=input("enter the second string")
    count=prefix(str1,str2)
    print("the prfix=",count)
main()