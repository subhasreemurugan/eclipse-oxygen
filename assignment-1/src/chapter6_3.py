def reverse(num):
    newnum=0
    while num>0:
        newnum=newnum*10+num%10
        num=num//10
    return newnum
def isPalindrome(n):
   
    num=reverse(n)
    if n==num:
        print("palindrome")
    else:
        print("not a plaindrome")
def main():
    n=eval(input("enter a number"))
    isPalindrome(n)
main()