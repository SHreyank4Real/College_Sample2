#Python Program to Put Even and Odd elements in a List into Two Different Lists
mainList = [1,2,3,4,5,6,7,8,9,10]
oddList = []
evenList = []

for i in mainList:
    if i%2 == 0:
        evenList.append(i)
    else:
        oddList.append(i)

print("Odd list",oddList)
print("Even list",evenList)