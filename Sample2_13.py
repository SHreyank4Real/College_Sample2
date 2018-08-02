#Python Program to Check if a Given Key Exists in a Dictionary or Not

dict1 ={'1':'hello','2':'World','3':'hell','4':'o'}
print(dict1)
key = str(input('enter key'))
data = dict1.get(key, "Key Not Found")
print(data)