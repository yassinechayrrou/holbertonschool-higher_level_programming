#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    directory_arr = dir(hidden_4)
    ignore = "__"
    for i in range(0, len(directory_arr)):
        if directory_arr[i][0] != ignore:
            print(directory_arr[i])
