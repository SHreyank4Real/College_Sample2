#Python Program to Remove the Duplicate Items from a List
list1 = [1,2,3,4,5,4,1,6,6,7,]
dublist = []

for i in list1:
    if i not in dublist:
        dublist.append(i)
print(dublist)