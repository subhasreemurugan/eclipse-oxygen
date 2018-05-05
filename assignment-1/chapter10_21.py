def merger(l1=[],l2=[]):
#     l=[]+l1+l2
#     print(l)
#     list1=l.sort()
#     print(l)
      
      size1=len(l1)
      size2=len(l2)
      list3=[]
      count=0
      for i in range(size1):
          for j in range(size2):
              if l1[i]>l2[j]:
                  list3.append(l2[j])
                  print()
              else:
                  list3.append(l1[1])
              count=count+1
              print(list3)
          
       
      print(list3)  
        
def main():
    s1=input("enter a sorted list")
    arr=s1.split()
    l1=[int(x) for x in arr]
    s2=input("enter second sorted list")
    arr=s2.split()
    l2=[int(x) for x in arr]
    
    merger(l1,l2)
main()