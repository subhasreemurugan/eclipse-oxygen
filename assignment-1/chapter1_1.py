curr=365*24*60*60
birth=curr//7
#print(birth)
death=curr//13
#print(death)
imm=curr//45
#print(imm)
population=birth+imm-death
#print(population)
firstYr=312032486+population
print(" first year", firstYr)
secondYr=firstYr+population
print(" second year", secondYr)
thirdYr=secondYr+population
print(" third year", thirdYr)
fourthYr=thirdYr+population
print("fourth year", fourthYr)
fifthYr=fourthYr+population
print("fifth year", fifthYr)

