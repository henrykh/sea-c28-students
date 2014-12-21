#!/usr/bin/env python

from lambda_magic import function_builder


def test_function_builder():
    the_list = function_builder(4)
    assert the_list[0](2) == 2
    assert the_list[1](2) == 3
    for i, f in enumerate(the_list):
        assert the_list[i](5) == 5+i
