#!/usr/bin/python3
ascii_pos = 0
for i in range(122, 96, -1):
    if i % 2 == 0:
        ascii_pos = i
    else:
        ascii_pos = i - 32
    print("{}".format(chr(ascii_pos)), end="")
