# def dectohex(s):
#     if s>=10:
#         c=s-10+ord('A')
#         print(s," this c",c)
#         print(chr(c))
#         return chr(c) 
#     else:
#         return s 
# def bintohex(bv):
#     print(bv+1)
#     arr=[]
#     i=0
#     arr.append(0)
#     arr.pop()
#     while(bv>0):
#         arr.append(bv%10)
#         bv=bv//10
#     print(arr)
#     count=digit=sum=0
#     finalstr=''     
#     for i in range(len(arr)):
#         count=count+1
#         digit=arr[i]*2**i
#         sum=digit+sum
#         
#         if(count%4==0):
#            print(sum)
#            c=dectohex(sum)
#            print(c,"this is c")
#            finalstr=finalstr+c
#            print(finalstr)
#            count=0
#            sum=digit=0
#     print(finalstr)
#         
# def main():
#   inp=input("enter a binary number")
#   str=''
#   if len(inp)%4 !=0:
#       zero=4-len(inp)%4
#       for i in range(zero):
#           str=str+'0'
#       inp=inp+str
#   intinp=int(inp)
#   print(intinp)
#   bintohex(intinp)
# main()




class Conversion:
    
    def reverse(self, a_string):
        new_string = ''
        index = len(a_string)
        while index:
            index -= 1                    
            new_string += a_string[index] 
        return new_string
        
    def binaryToDecimal(self, number):
        result = ''
        strRev = self.reverse(number)
        for i in range(0, len(strRev),4) :
            print(i)
            fourDigit = strRev[i : i + 4]
            print(fourDigit)
            sumOfFour = 0
            for j in range(0,len(fourDigit)) :
                if fourDigit[j] == '1':
                    sumOfFour += 2 ** j
            sumOfFour = str(sumOfFour)        
            if sumOfFour == '10' :
                sumOfFour = 'A'
            if sumOfFour == '11' :
                sumOfFour = 'B'
            if sumOfFour == '12' :
                sumOfFour = 'C'
            if sumOfFour == '13' :
                sumOfFour = 'D'
            if sumOfFour == '14' :
                sumOfFour = 'E'
            if sumOfFour == '15' :
                sumOfFour = 'F'
            
            result  += sumOfFour          
        return self.reverse(result)
        
number = input("Enter a binary number : ")
conversion = Conversion()
print("Hexadecimal for the binary is : " + str(conversion.binaryToDecimal(number)))

