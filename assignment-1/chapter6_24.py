def reverse(num):
    newnum=0
    while num>0:
        newnum=newnum*10+num%10
        num=num//10
    return newnum
def primeno(num):
    for i in range(2,int(num)):
        if(num%i==0):
            return 'false'
        
    return 'true'
def isPalindrome(n):
    num=reverse(n)
    if n==num:
        return 'true'
    else:
       return 'false'
def main():
   count=0
   i=2
   while count<100:  
       if primeno(i)=='true' and isPalindrome(i)=='true' :
           count=count+1
           print(format(i,'10d'),end=' ')
           if count%10==0:
               print()
       i=i+1  
   print("end")  
main()