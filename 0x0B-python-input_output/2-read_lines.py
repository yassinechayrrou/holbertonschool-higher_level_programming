#!/usr/bin/python3
def read_lines(filename="", nb_lines=0):
    with open(filename, encoding="utf-8") as f:
        fr = f.read()
        if nb_lines == 0:
            print(fr, end="")
        else:
            for line in f:
                if 0 < nb_lines:
                    print(line, end="")
                    nb_lines -= 1
