#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4

    names = dir(hidden_4)
    new_names = [name for name in names if not name.startswith("__")]
    sort_names = sorted(new_names)
    for i in sort_names:
        print(i)
