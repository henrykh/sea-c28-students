#!/usr/bin/env python

from series import fibonacci, lucas, sum_series


def test_fibonacci():
    fibonacci_first_eight = [0, 1, 1, 2, 3, 5, 8, 13]

    for number in range(1, 9):
        assert fibonacci(number) == fibonacci_first_eight[number-1]


def test_lucas():
    lucas_first_eight = [2, 1, 3, 4, 7, 11, 18, 29]

    for number in range(1, 9):
        assert lucas(number) == lucas_first_eight[number-1]


def test_sum_series():

    for number in range(1, 9):
        # test whether calling sum_series() without parameters returns the same value as fibonacci(), given n
        assert sum_series(number) == fibonacci(number)

        # test whether calling sum_series() with the parameters 2,1 returns the same value as lucas(), given n
        assert sum_series(number, 2, 1) == lucas(number)

    # test whether calling sum_series() with different parameters returns the expected result
    assert sum_series(3, first=5, second=4) == 9
    assert sum_series(4, first=3, second=3) == 9
    assert sum_series(5, first=6, second=7) == 33
