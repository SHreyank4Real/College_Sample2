#Python Program to Multiply All the Items in a Dictionary

dict1 ={'one':1,'two':2,'three':3,'four':4,'five':5}
product=1
for i in dict1:
    product=product*int(dict1[i])

print("Sum of values is :",product)