filname=input("enter the file name(myfile.txt)")

file1=open(filname,'w')
cont=input("word to be removed")
file1.write("hello good morning this  morning is beautiful  ")
file1.close()
file2=open(filname,'r')
line=file2.read()
print(line)
list1=[(x) for x in line.split()]
file2.close()
# print(list1)
file1=open(filname,'w')
for x in list1:
    if x==cont:
        list1.remove(cont)
    else:
        file1.write(x+" ")
file1.close()
file2=open(filname,'r')
line=file2.read()
file2.close()
# print(line)
print(list1)
