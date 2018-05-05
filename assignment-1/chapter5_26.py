m=1
k=3
sum=0
for i in range(m,49):
    sum=sum + m/k
    print(m,'/',k ,"+",end="")
    m=m+2
    k=k+2
print(sum)