#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    my_list = sorted(a_dictionary.keys())
    for i in my_list:
        print("{:s}: {}".format(i, a_dictionary[i]))
