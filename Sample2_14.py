#Python Program to Generate a Dictionary that Contains Numbers (between 1 and n) in the Form (x,x*x).

n = int(input("value of n: " ))
dict1 = {}
for i in range(1,n+1):
    dict1[i]=i*i

print(dict1)