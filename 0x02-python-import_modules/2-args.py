#!/usr/bin/python3
import sys
argv = sys.argv
argc = len(sys.argv)
if __name__ == "__main__":
        if argc == 1:
                print("0 arguments.")
        else:
                print(argc - 1, ("arguments:", "argument:")[argc == 2])
                for i in range(1, argc):
                        print("{}: {}".format(i, argv[i]))
