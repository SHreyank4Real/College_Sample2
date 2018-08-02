#Python Program to Read a List of Words and Return the Length of the Longest One.
words = str(input("Enter the words using space inbetween"))
words = words.split(' ')
print(words)
big = 0
word = ''
for i in words:
    if len(i) > big:
        big = len(i)
        word = i
print("largest word is ",word,"Length is ",big)