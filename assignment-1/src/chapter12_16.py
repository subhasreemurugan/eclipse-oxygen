class stack(list):
    def __init__(self,list1=[]):
        self.list1=list1
    def push(self,x):
        self.list1.append(x)
        return self.list1
    def pop(self):
        x=self.list1.pop()
        return x
    def getlist(self):
        print(self.list1)
def main():
    list1=[]
    l=stack(list1)
    print("choice  1.push 2.pop 3.print list 4.exit")
    opt=1
    while opt >=1 and opt<=4:
        opt=eval(input("enter your choice"))
        if opt==1:
            a=eval(input("enter val"))
            l.push(a)
        elif opt==2:
            b=l.pop()
            print("poped",b)
        elif opt==3:
            l.getlist()
        else:
            print("thankyou")
            break
            
    
main()