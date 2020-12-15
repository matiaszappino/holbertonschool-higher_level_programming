#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    tuple_c = ()
    appending_a = []
    appending_b = []

    if len(tuple_a) >= 2 and len(tuple_b) >= 2:
        tuple_c = (tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1])
    else:
        if len(tuple_a) == 1:
            appending_a.append(tuple_a[0])
            appending_a.append(0)
        if len(tuple_b) == 1:
            appending_b.append(tuple_b[0])
            appending_b.append(0)
        if len(tuple_a) == 0:
            appending_a.append(0)
            appending_a.append(0)
        if len(tuple_b) == 0:
            appending_b.append(0)
            appending_b.append(0)
        if len(appending_a) == 0:
            appending_a.append(tuple_a[0])
            appending_a.append(tuple_a[1])
        if len(appending_b) == 0:
            appending_b.append(tuple_b[0])
            appending_b.append(tuple_b[1])
        tuple_c = (appending_a[0] + appending_b[0], appending_a[1] + appending_b[1])
    return tuple_c
