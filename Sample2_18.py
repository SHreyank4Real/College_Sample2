#Write a function is_empty(my_dict) that takes a dictionary my_dict and
# returns True if my_dict is empty and False otherwise

def is_empty(my_dict):
    if my_dict:
        return False
    else:
        return True

my = {}

print(is_empty(my))