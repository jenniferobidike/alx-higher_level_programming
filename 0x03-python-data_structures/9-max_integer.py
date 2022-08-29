#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) == 0:
        return (None)

    max_big = my_list[0]
    for i in range(len(my_list)):
        if my_list[i] > max_big:
            max_big = my_list[1]

            return max_big
