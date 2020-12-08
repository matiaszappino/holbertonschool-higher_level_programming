def uppercase(str):
    for i in range(len(str)):
        letter = ord(str[i])
        if letter >= 97 and letter <= 121:
            print("{:c}".format(letter - 32), end="")
        else:
            print("{:c}".format(letter), end="")
