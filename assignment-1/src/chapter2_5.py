amt=eval(input("Enter the monthly saving amount"))
tot_amt=0
for i in range (6):
    
    tot_amt=(tot_amt+amt)*(1+0.00417)
print("After six month saving amount:",format(tot_amt,'10.2f'))
