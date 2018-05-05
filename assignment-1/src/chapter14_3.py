'''
Created on Sep 24, 2017

@author: mssub
'''
import os.path
import sys
print("hi")
dict={"and":"0","for":"0","if":"0"}
filnam=input("enter the file name")
if not os.path.isfile(filnam):
    print("file does not exist")
    sys.exit()
file1=open(filnam,'r')
f1=file1.read()
line=f1.split()
print(line)
for x in line:
#     print(x)
    if x in dict.keys():
        dict[x]=str(int(dict[x])+1)
file1.close()
print(dict)