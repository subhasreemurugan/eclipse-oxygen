'''
list1=list()
list1.append(10)
list1.insert(0,1)
list1.remove(10)
list1.append(11)
# list1.append("color")
list1.index(1) 
  
list1.sort()
print(list1," ",list1.index(1),sum(list1))
 
l1=[x for x in range(10)if x%3==0]
print(l1)
'''
# def countLetters(s):
#     result = 0
#     for i in s:
#         if ord(i) > ord('a') or ord(i) > ord('A') and ord(i) < ord('z') or ord(i) < ord('Z'):
#             result += 1    
#     print(result)
#        
# s = input("Enter a string/statement: ")
# countLetters(s)


# def main():
#     x = 1 # x represents an int value
#     y = [1, 2, 3] # y represents a list 
#     m(x, y) # Invoke f with arguments x and y
#     print("x is " + str(x))
#     print("y[0] is " + str(y[0]))
# 
# def m(number, numbers):
#     pass
#     number = 1001 # Assign a new value to number
#     numbers[0] = 5555 # Assign a new value to numbers[0]
# 
# main()


'''

def add(x, lst = []):
    if not(x in lst):
        lst.append(x)
    return lst
list1 = add(1)
print(list1)
list2 = add(2)
print(list2)
list3 = add(3, [11, 12, 13, 14])
print(list3)
list4 = add(4)
print(list4)


matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]] # Assume a list is given
for column in range(len(matrix[0])):
     total = 0
     for row in range(len(matrix)):
          total += matrix[row][column] 
          print("Sum for column", column, "is", total)
'''
def rev(num):
    x = 0
    while num > 0:
        x = x * 10 + num % 10
        num = num // 10
    return x

def main():
    list1 = input("Enter list of integers: ")
    list2 = list1.split()
    l3 = [eval(x) for x in list2]
    print(l3)
    for i in range(len(l3)):
        l3[i] = (rev(l3[i]))
    print("Reversed List: ", l3)
    
main()    
