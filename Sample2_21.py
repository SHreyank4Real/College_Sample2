'''Write a function make_cipher_dict(alphabet) that takes a string of unique characters and returns a
randomly-generated cipher dictionary for the characters in alphabet . You should use the shuffle()
method in the random module to ensure that your returned cipher dictionary is random'''

import random
import string

def make_cipher_dict():
    String = str(input("Enter the String "))
    nString = ''
    for i in String:
        if i not in nString:
            nString +=i
    #String = set(String)
    #String = str(String)
    print(nString)
    ShuffleStr(nString)

def ShuffleStr(nString):
    dict_cipher={}
    #nS =S
    for i in nString:
        dict_cipher[i] = random.choice(string.ascii_lowercase)
    print("Cipher Dictionary is :")
    print(dict_cipher)
    Display_Cipher(dict_cipher,nString)


def Display_Cipher(dict1,St):
    FS = ""
    for i in St:
        FS = FS+dict1[i]
    print(FS)


make_cipher_dict()
