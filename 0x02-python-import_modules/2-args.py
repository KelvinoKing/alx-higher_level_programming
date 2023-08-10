#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    num_args = len(sys.argv)
    if num_args == 1:
        print("0 arguments.")
    elif num_args == 2:
        print(f"{num_args - 1} argument:")
    else:
        print(f"{num_args - 1} arguments:")
    for i in range(1, len(sys.argv)):
        print(f"{i}: {sys.argv[i]}")
