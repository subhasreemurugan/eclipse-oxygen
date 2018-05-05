import random
lottery=random.randint(100,1000)
l1=lottery
n=int(input("enter the lottery no"))
l2=n
print(lottery)
arr=[{0}]
lotr=[{0}]
arr.pop()
lotr.pop()
while n>0:
    arr.append(n%10)
    n=n//10
while lottery>0:
    lotr.append(lottery%10)
    lottery=lottery//10
print(arr," ",lotr," ")
if l1==l2:
    print("you win!! matches the lottery number in the exact order, the award is $10,000. ",n,lottery)  
else:
    
    if (lotr[0]==arr[0] or lotr[0]==arr[1] or lotr[0]==arr[2] )and (lotr[1]==arr[0] or lotr[1]==arr[1] or lotr[1]==arr[2]) and( lotr[2]==arr[0] or lotr[2]==arr[1] or lotr[2]==arr[2]):
        print(" digits in the user input match all the digits in the lottery number, the award is $3,000 ")
    elif (lotr[0]==arr[0] or lotr[0]==arr[1] or lotr[0]==arr[2] or lotr[1]==arr[0] or lotr[1]==arr[1] or lotr[1]==arr[2] or lotr[2]==arr[0] or lotr[2]==arr[1] or lotr[2]==arr[2]):
        print(" one digit in the user input matches a digit in the lottery number, the award is $1,000")
    else:
        print("nothing matched")