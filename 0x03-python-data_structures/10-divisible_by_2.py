#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    len_list = len(my_list)
    if len_list == 0:
        return None
    else:
        new_list = []
        for i in my_list:
            if i % 2 == 0:
                new_list.append(True)
            else:
                new_list.append(False)

    return new_list
