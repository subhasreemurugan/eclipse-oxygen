pas=(input("enter your password"))
dig=0
for i in pas:
    if ord(i)>ord('0') and ord(i)<ord('9'):
#         print(ord(i))
        dig =dig+1
# print(len(pas),pas.isalnum(),dig)
if len(pas)>8 and pas.isalnum() and dig>=2:
    print("valid")
else:
    print("not valid")