# Chap2.2.9
# twc = 35.74 + 0.6215*5.3 - 35.75*(6**.16) + 0.4275*5.3*(6**.16)
# print(twc)

# chapter2    2.12
# j=1
# for i in range(5):
#   print(j, " ",j+1," ",j**(j+1))
#   j=j+1
# print(format(3*(3**(1/2))/2*(5.5**2),'10.4f'))
import time
randomSeed=time.time()
randomNumber = int(randomSeed % 26) + 65
print(chr(randomNumber))