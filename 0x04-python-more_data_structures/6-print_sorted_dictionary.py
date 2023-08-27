#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    if a_dictionary is not None:
        my_list = sorted(a_dictionary.keys())
        for i in my_list:
            print("{:s}: {}".format(i, a_dictionary[i]))
