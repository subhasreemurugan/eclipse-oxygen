n=eval(input("enter number"))
k=0
q=n
for i in range(n):
     
    for j in range(n,1,-1):
        print(end="  ")
    
    for q in range(i+1,1,-1):
        print(q,end=" ")
       
    for k in range(i+1):
        print(k+1,end=" ")

     
    print() 
    n=n-1
    
