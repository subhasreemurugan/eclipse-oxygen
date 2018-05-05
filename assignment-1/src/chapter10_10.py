import random
m1=[]
m2=[]

for i in range(4):
    m2.append([])
    for j in range(4):
        m2[i].append(random.randint(0,1))
print(m2)
maxsum = sum(m2[0])
for i in range(1,4):
    if maxsum<sum(m2[i]):
        maxsum=sum(m2[i])
        row=i
print("max row is",maxsum,"The largest row index. ",row)
larg=-1
col=0
for i in range(4) :
    tot=0
    for j in range(4):
        tot=tot+m2[j][i]
    if(tot>larg): 
        larg=tot
        col=i 
print("large column sum ",larg," The largest column index",col)