#!/usr/bin/python3
def common_elements(set_1, set_2):
    result = []
    for i in set_1:
        if i in set_2:
            result.append(i)
    for i in set_2:
        if i in set_1 and i not in result:
            result.append(i)
    return result
