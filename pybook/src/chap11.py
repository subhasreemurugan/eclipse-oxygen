list1=[[1,2],[1,3],[1,5]]
for i in range(len(list1)):
    for x in range(len(list1[i])):
        print(list1[i][x],end=' ')
    print()
for row in list1:
    for col in row:
        print(col,end=' ')
    print()