#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    counter = 0
    result = []
    for i in range(0, list_length):
        try:
            c = my_list_1[i] / my_list_2[i]
        except(TypeError):
            print("wrong type")
            c = 0
        except(ZeroDivisionError):
            print("division by 0")
            c = 0
        except(IndexError):
            print("out of range")
            c = 0
        finally:
            result.append(c)
    return result
