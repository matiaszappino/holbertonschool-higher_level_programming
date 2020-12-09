#!/usr/bin/python3
for i in range(122, 96, -1):
    letter = chr(i)
    if i % 2 == 0:
        print("{}".format(letter), end="")
    else:
        letter = chr(i - 32)
        print("{}".format(letter), end="")
