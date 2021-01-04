#!/usr/bin/python3
def safe_function(fct, *args):
    import sys
    try:
        a = args[0]
        b = args[1]
        c = fct(a, b)
    except Exception as e:
        c = None
        string = "Exception: " + str(e) + '\n'
        sys.stderr.write(string)
    return c
