#Python Program to Concatenate Two Dictionaries Into One

dict1 = {'1':'one','2':'two','3':'three'}
dict2 = {'4':'four','5':'five','6':'six'}
print(dict1)
print(dict2)

dict1.update(dict2)
dict2.clear()
print(dict1)