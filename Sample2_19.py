#Write a function make_dict(key_value_list) that takes a list of tuples key_value_list where
# each tuple is of the form (key, value) and returns a dictionary with these keys and
# corresponding values


def make_dict(key_value_list):
    my_dict = {}
    for i,j in key_value_list:
        my_dict[i] = j
    print(my_dict)


my = [('one',1),('two',2),('three',3),('four',4),('five',5),('six',6)]
make_dict(my)