#!/usr/bin/python3
def safe_function(fct, *args):
    import sys
    try:
        a = args[0]
        b = args[1]
        c = fct(a, b)
        return c
    except Exception as e:
        string = "Exception: " + str(e) + '\n'
        sys.stderr.write(string)
        return None
