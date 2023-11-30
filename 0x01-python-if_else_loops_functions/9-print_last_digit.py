#!/usr/bin/python3
def print_last_digit(number):
    if number > 0:
        return number%10
    else:
        value = 0 - (10 - number%10)
        return value
