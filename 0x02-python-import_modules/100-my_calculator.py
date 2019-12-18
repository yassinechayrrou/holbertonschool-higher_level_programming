#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    from sys import argv
    argc = len(argv) - 1
    if argc != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    n = int(argv[1])
    m = int(argv[3])
    if argv[2] == "+":
        print("{} + {} = {}".format(n, m, add(n, m)))
    elif argv[2] == "-":
        print("{} + {} = {}".format(n, m, sub(n, m)))
    elif argv[2] == "*":
        print("{} + {} = {}".format(n, m, mul(n, m)))
    elif argv[2] == "/":
        print("{} + {} = {}".format(n, m, div(n, m)))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
