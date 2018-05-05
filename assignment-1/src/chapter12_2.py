class location:
    def __init__(self,noOfRows=2,noOfColumn=2,maxVal=0):
        self.noOfRows=noOfRows
        self.noOfColumn=noOfColumn
        self.maxVal=maxVal
    def output(self):
        print("max is ",self.maxVal,"at the location",self.noOfRows,self.noOfColumn)
   
   
def main():
    list1=[]
    noOfRows=eval(input("enter non of rows"))
    noOfColumn=eval(input("enter the no of columns"))
    for j in range(noOfRows):
        line=input("enter the row list").strip().split();
        list1.append([eval(x) for x in line])
   
    print(list1) 
    l=locateLargest(list1) 
    l.output()
def  locateLargest(a):
    maxVal=a[0][0]
    for i in range(len(a)):
        for j in range(len(a)):
            if(maxVal<a[i][j]):
                maxVal,a[i][j]=a[i][j],maxVal
                noOfRows,noOfColumn=i,j
    return location(noOfRows,noOfColumn,maxVal)
                
main()               
            
        
        
        