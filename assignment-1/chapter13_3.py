filname=input("enter the file name(myfile.txt)")
file1=open(filname,'w')
file1.write("hello  23 good morning this 45  morning is beautiful  ")
file1.close()
file1=open(filname,"r")
f=file1.read()
s=scores=0
for x in f.split():
    if x.isdigit()==True:
        scores=scores+1
        s=s+int(x)
print("the scores are",scores)
print("the sum",s)

file1.close()
