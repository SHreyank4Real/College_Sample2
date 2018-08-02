#Python Program to Find the Largest Number in a List
import random

ran=int(input("Enter the range"))
lis = []
for i in range(ran):
    lis.append(random.randint(1,100))
print(lis)
lis.sort()

print("Largest number is ",lis[-1])
