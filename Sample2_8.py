#Python Program to Create a List of Tuples with the First Element as the Number and Second Element as the Square of the Number
list1 = []
for i in range(1,10):
    list1.append((i,i*i))

print(list1)