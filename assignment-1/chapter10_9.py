def mean(l1 =[]):
    sum=0
    for i in l1:
        sum=sum+i
    return (sum/len(l1))
def dev(l1=[]):
    m = mean(l1)
    d=0
    for i in l1:
       d=(( i-m)**2)+d
    return (d/(len(l1)-1))**0.5
def main():
    s=input("enter thelist")
    arr=s.split()
    l1=[eval(x) for x in arr]
    print(l1)
    print("mean",mean(l1))
    print("std deveiation",dev(l1))
main()