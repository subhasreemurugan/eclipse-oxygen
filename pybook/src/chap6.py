def sumno(a,b):
    result=0
    for i in range(a,b+1):
        result=result+i
        print("ji",result)
    return result
def grade(x):
    if x>90:
       print("a")
       gradegot='A'
    else:
        print("B")
        gradegot='B'
#     return gradegot
    
def main():
#     print("hello")
#     result1=sumno(10,20)
#     print("heool")
    score=eval(input("enter the score"))
#     g=grade(score)
    print(grade(score))  
    ''' print NONE  is a keyword 
    grade(x=90) 
     '''
#     print(g)
main()


#decimal to hexadeci
