#Python Program to check whether two lists are same
list1 = [1,2,3,4,5,6,7,8]
list2 = [1,2,3,4,5,6,7,9]
flag = True

if len(list1)!=len(list2):
    print("Not equal")
else:
    for i in range(len(list1)):
        if list1[i] == list2[i]:
            pass
        else:
            flag = False

if flag == True:
    print("Lists are same")
else:
    print("Not Same")