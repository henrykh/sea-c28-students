#!/usr/bin/env python

import pytest

from ack import ack


def test_ack():
    # ack_dict = {x,y: z for x in range(4) y in range(5)}
    ackermann_dict = {(0, 0): 1, (0, 1): 2, (0, 2): 3, (0, 3): 4,
                      (0, 4): 5, (1, 0): 2, (1, 1): 3, (1, 2): 4,
                      (1, 3): 5, (1, 4): 6, (2, 0): 3, (2, 1): 5,
                      (2, 2): 7, (2, 3): 9, (2, 4): 11, (3, 0): 5,
                      (3, 1): 13, (3, 2): 29, (3, 3): 61, (3, 4): 125}

    for m in range(4):
        for n in range(5):
            assert (ack(m, n)) == ackermann_dict[m, n]


def test_ack_type_error():
    with pytest.raises(TypeError):
        ack('a', 'b')


def test_ack_negative():
    assert ack(-1, -1) is None
