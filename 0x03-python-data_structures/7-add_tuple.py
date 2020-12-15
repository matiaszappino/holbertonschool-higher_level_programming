#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    tuple_c = ()
    appenda = []
    appendb = []

    if len(tuple_a) >= 2 and len(tuple_b) >= 2:
        tuple_c = (tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1])
    else:
        if len(tuple_a) == 1:
            appenda.append(tuple_a[0])
            appenda.append(0)
        if len(tuple_b) == 1:
            appendb.append(tuple_b[0])
            appendb.append(0)
        if len(tuple_a) == 0:
            appenda.append(0)
            appenda.append(0)
        if len(tuple_b) == 0:
            appendb.append(0)
            appendb.append(0)
        if len(appenda) == 0:
            appenda.append(tuple_a[0])
            appenda.append(tuple_a[1])
        if len(appendb) == 0:
            appendb.append(tuple_b[0])
            appendb.append(tuple_b[1])
        tuple_c = (appenda[0] + appendb[0], appenda[1] + appendb[1])
    return tuple_c
