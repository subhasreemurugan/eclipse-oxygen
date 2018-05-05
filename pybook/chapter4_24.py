import random
card=random.randint(1,52)
type=card%13
suit=card%3
if type==1:
    card='ace'
elif type==11:
    card='jack'
elif type==12:
    card='queen'
elif type==1:
    card='king'
if suit==0:
    suit='clubs'
elif suit==1:
    suit='diamond'
elif suit==2:
    suit='hearts'
elif suit==3:
    suit='spade'
print("The card you picked is the ",type," of",suit)