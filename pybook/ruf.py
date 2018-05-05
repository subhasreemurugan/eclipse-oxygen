# def binaryToHex(bv):
# #    for bv>0:
# #        dig=bv%10 + dig
# #        count=count+1
# #        if count>=4:
# #            bintodec()
#     count=0
#     for i in range(bv,0,-1):
#         p=bv[i]
#         dig = int(p)*10+dig
#         count=count+1 
#         tot=bv[i]*2**count
#         if tot >=10 or tot<17:
#            tot=10-ord(i)+ord('A') 
#         sum=str(tot)+sum
#         if i%4==0:
#             dig =0
#             count=0
1111==1*2**loction+1*2**(loc+1)



def binaryToHex(bv):
    i=0
    
    while bv>0:
       
        digit[i]=bv%10
        i=i+1
        bv=bv//10
    print(digit)   
        
def main():
    inp=int('1111')
    binaryToHex(inp)          
    
main()



# priyanka code
# 
# def isPrimeNumTest(num):
#         
#     for i in range(2,int(num)):
#         if(num%i==0):
#             return False  
#     return True
#             
# def reverse(x):
#     return str(x)[::-1]
# 
# def checkPalindrome(x):
#     rev = reverse(x)
#     if int(x) == int(rev):
#         return True
#     else:
#         return False
# 
# #checkPalindrome(1221)
# 
# def palindromicPrime():
#     i=2
#     count=0
#     while count<=100:
#         print("count",count,checkPalindrome(count),isPrimeNumTest(count))
#         if checkPalindrome(count) and isPrimeNumTest(count):
#             print(i)
#         count+=1
#         
# 
# # x = eval(input("Numbers to be printed : "))
# palindromicPrime()
