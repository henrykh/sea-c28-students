#!/usr/bin/env python

def function_builder(n):
    """return a list of n lambda functions"""

    return [lambda x, y=number:x+y for number in range(n)]

if __name__ == "__main__":

    the_list = function_builder(4)
    print the_list[0](2)
    print the_list[1](2)
    for f in the_list:
        print(f(5))
