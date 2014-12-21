#!/usr/bin/env python

from iterator_1 import IterateMe_2


def test_IterateMe_2_start():
    it = IterateMe_2(5, 10)
    assert it.next() == 5


def test_IterateMe_2_stop():
    it = IterateMe_2(0, 10)
    for i in it:
        pass
    else:
        assert i == 9


def test_IterateMe_2_step():
    it = IterateMe_2(0, 10)
    for i, x in zip(it, range(0, 10)):
        assert i == x

    it2 = IterateMe_2(0, 10, 2)
    evens = [x for x in range(0, 10) if x == 0 or x % 2 == 0]
    for i, x in zip(it2, evens):
        assert i == x


def test_IterateMe_2_break():
    it = IterateMe_2(2, 20, 2)

    xit = xrange(2, 20, 2)

    for i, x in zip(it, xit):
        if i > 10:
            break
        assert i == x
    for i, x in zip(it, xit):
        assert i == x
