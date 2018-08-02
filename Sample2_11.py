#Python Program to Add a Key-Value Pair to the Dictionary
print("Capitals dictonary of len 3")
capital = {} #empty dict

for i in range(3):
    key = input("Enter country :")
    value = input("Enter capital")
    capital[key] = value

print(capital)