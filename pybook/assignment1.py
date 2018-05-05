# # letter from user and convert to uppercase
# charac=input("enter a character")
# charac=ord(charac)-32
# print("the uppercase of the character is",chr(charac))
# 
# #write a prog that random uppercaes using time
# print((95.5*0.45359237)/((50*0.0254)**2))
import time

offset =eval( input("Enter the time zone offset to GMT: "))

currentTime = time.time()
totalSeconds = int(currentTime)
currentSecond = totalSeconds % 60
totalMinutes = totalSeconds // 60
currentMinute = totalMinutes % 60
totalHours = totalMinutes // 60
currentHour = (totalHours % 24) 
print("Current time is: " ,  ((currentHour + offset) % 24) , ":" , (currentMinute) , ":" , (currentSecond) , "GMT")