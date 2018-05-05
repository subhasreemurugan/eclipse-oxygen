# n=eval(input("enter number"))
# k=0
# q=n
# for i in range(n):
#       
#     for j in range(n,1,-1):
#         print(end="  ")
#      
#     for q in range(i+1,1,-1):
#         print(q,end=" ")
#         
#     for k in range(i+1):
#         print(k+1,end=" ")
#  
#       
#     print() 
#     n=n-1
#      
# def reverse(number):
#     
#     return str(number)[::-1] #== number
#     
# def isPalindrome(number):
#     rev = reverse(number)
#     
#     if int(number) == int(rev):
#         #return True
#         print("Entered number is a palindrome")
#     else:
#         #return False
#         print("Entered number is not a palindrome")
#         
# x = eval(input("Enter a number to check if it's a Palindrome: "))
# reverse(x)
# isPalindrome(x)

# prime fcatros
# n=eval(input("enter the number"))
# sq1=int(n**0.5+1)
# 
# 
# for i in range(2,n):
#    
#     while (n%i) == 0:
#         print(i)
#         n=n//i

 
n=9
k=0

for i in range(n):
       
    for j in range(n-1):
        print(end="     ")
    no=1  
    for q in range(i+1):
        print(no,end="    ")
        no=no*2
    no=2**i     
    for k in range(1,i+1):
        no=int(no/2)
        print(no,end="    ")
        
       
        
   
        
    print() 
    n=n-1