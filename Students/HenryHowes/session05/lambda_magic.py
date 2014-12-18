#!/usr/bin/env python

def function_builder(n):
    """return a list of n lambda functions"""

    return [lambda x, y=number:x+y for number in range(n)]

if __name__ == "__main__":

    the_list = function_builder(4)
    assert the_list[0](2) == 2
    assert the_list[1](2) == 3
    for i, f in enumerate(the_list):
        assert (f(5)) == i+5

    print "All tests passed"