import random
comp=0
user=0
while comp<2 and user<2 :
    ch=eval(input("enter your choice"))
    comp_ch=random.randint(0,3)
    if(comp_ch>ch):
        comp=comp+1
        print("computer wins")
    else:
        user=user+1
        print("you win")
    if comp==2 or user==2:
        print("thank you")
        break
    