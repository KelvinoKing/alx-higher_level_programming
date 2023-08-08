#!/usr/bin/python3
j = 0
for i in range(0, 9):
    j += 1
    for k in range(j, 10):
        if (i != 8 and k != 9):
            if (i != k):
                print("{}{}, ".format(i, k), end="")
        elif (i != 8 and k == 9):
            print("{}{}, ".format(i, k), end="")
        elif (i == 8 and k == 9):
            print("{}{}".format(i, k))
