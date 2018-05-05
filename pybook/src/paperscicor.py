def val(x):
    if x==0:
        txt='scissor'
    elif x==1:
        txt='rock'
        
    elif x==2:
        txt='paper'
    return txt

import random
comp=random.randint(0,2)
urs=eval(input("enert"))
if urs>comp:
    print("cmp",val(comp),"urs",val(urs),"thus u win")
elif urs==comp:
    print("cmp",val(comp),"urs",val(urs),"draw")
else:
    print("cmp",val(comp),"urs",val(urs),"i win")

