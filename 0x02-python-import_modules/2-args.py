#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    ac = len(sys.argv) - 1
    argv = sys.argv
    if ac == 0:
        print("{} arguments.".format(ac))

    elif ac == 1:
        print("{} argument:".format(ac))
        print("{}: {}".format(ac, argv[1]))

    else:
        print("{} arguments:".format(ac))
        for i in range(1, len(argv)):
            print("{}: {}".format(i, argv[i]))
