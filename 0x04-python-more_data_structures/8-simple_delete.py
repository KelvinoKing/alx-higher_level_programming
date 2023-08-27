#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    if a_dictionary is not None:
        new_dict = a_dictionary
        key_list = list(a_dictionary)
        for i in key_list:
            if i == key:
                del new_dict[key]
        return new_dict
