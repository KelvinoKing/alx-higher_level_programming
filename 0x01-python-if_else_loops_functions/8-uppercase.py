#!/usr/bin/python3
def uppercase(str):
    for i in range(len(str)):
        if (ord(str[i]) > 96 and ord(str[i]) < 123):
            str = str.replace(str[i], chr(ord(str[i]) - 32))
        else:
            continue

    print("{}".format(str))
