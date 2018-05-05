import os.path
import sys
print("hi")

filnam=input("enter gthe file name")
if not os.path.isfile(filnam):
    print("file does not exist")
    sys.exit()
file1=open(filnam,'r')
f1=file1.read()
vow={'a','e','i','o','u'}
count1=0
for x in f1:
#     print(x)
    if x in vow:
        print(x)
        count1=1+count1
print(count1)