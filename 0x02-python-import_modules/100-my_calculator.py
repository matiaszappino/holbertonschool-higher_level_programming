#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    import sys
    argv = sys.argv
    ac = len(sys.argv) - 1
    if ac != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    op = argv[2]
    if op == "+" or op == "-" or op == "*" or op == "/":
        a = int(argv[1])
        b = int(argv[3])

        if op == "+":
            print("{} {} {} = {}".format(a, op, b, add(a, b)))
        if op == "-":
            print("{} {} {} = {}".format(a, op, b, sub(a, b)))
        if op == "*":
            print("{} {} {} = {}".format(a, op, b, mul(a, b)))
        if op == "/":
            print("{} {} {} = {}".format(a, op, b, div(a, b)))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1) 
