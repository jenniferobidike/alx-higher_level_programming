#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) == 0:
        return (None)

    max_big = my_list[0]
    for i in my_list:
        if i > max_big:
            max_big = i

            return max_big
