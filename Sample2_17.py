#Python Program to Remove the Given Key from a Dictionary

dict1 ={'1':'hello','2':'World','3':'hell','4':'o'}
print(dict1)
key = str(input('enter key'))
del dict1[key]
print("After deleteing \n ",dict1)