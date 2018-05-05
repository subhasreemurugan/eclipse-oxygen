noStud=eval(input("enter no of student"))
highest=0
for i in range(noStud):
    score=eval(input("enter the score"))
    if highest < score:
        h2=highest
        highest=score
         
    elif score>h2:
        h2=score
print("highest",highest,"2nd highest",h2)
         
# no=1
# i=1
# while no<12000:
#     no=i*i
#     i=i+1
# print(i)