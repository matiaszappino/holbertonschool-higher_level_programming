#!/usr/bin/python3
def weight_average(my_list=[]):
    num = 1.0
    first = []
    res = []
    if not my_list:
        return 0
    else:
        for i in my_list:
            for j in range(len(i)):
                num = num * i[j]
                if j + 1 == len(i):
                    res.append(i[j])
                    first.append(num)
            num = 1.0
        return float(sum(first)) / float(sum(res))
