#!/usr/bin/python8
def print_last_digit(number):
    last = 0

    last = abs(number) % 10
    print(last, end="")
    return last
