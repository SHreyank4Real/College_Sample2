#Python Program to Sum All the Items in a Dictionary
dict1 ={'one':1,'two':2,'three':3,'four':4,'five':5}
sum=0
for i in dict1:
    sum=sum+int(dict1[i])

print("Sum of values is :",sum)