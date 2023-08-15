#!/usr/bin/python3
def max_integer(my_list=[]):
    list_len = len(my_list)

    if list_len == 0:
        return None
    temp = my_list[0]
    if list_len == 1:
        return my_list[0]
    else:
        for j in range(1, list_len):
            if temp < my_list[j]:
                temp = my_list[j]

        return temp
