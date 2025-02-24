#!/usr/bin/python3
def uniq_add(my_list=[]):
    new_list = []
    total = 0
    for i in my_list:
        if i in new_list:
            pass
        else:
            new_list.append(i)
            total = total + i
    return total
