  
a,b=eval(input("enter 2 nos a,b"))
gcd=1
k=2
while k<=a and k<=b:
    if a%k==0 and b%k==0:
        gcd=k 
    k=k+1
print("gcd",gcd)

# # factors
# a=int(input("enter a no"))
# for i in range(2,a+1):
# #   print(i)
#   if a%i==0:
# #     print(i,"inside")
#     a=a//i
#     print(a,"op")
#     i=i-1
# # print(a,"out")
