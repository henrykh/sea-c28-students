#!/usr/bin/env python

def count_evens(int_array):
    """return the number of even numbers in the array"""

    return sum([1 for a in int_array if a % 2 == 0])


if __name__ == '__main__':
    print count_evens([2, 1, 2, 3, 4])
    print count_evens([2, 2, 0])
    print count_evens([1, 3, 5])
