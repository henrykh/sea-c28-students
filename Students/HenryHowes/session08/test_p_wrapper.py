#!/usr/bin/env python

from p_wrapper_decorator import p_wrapper


def test_p_wrapper():

    @p_wrapper
    def return_a_string(string):
        return string

    @p_wrapper
    def string_five(string):
        return string*5

    assert return_a_string("this is a string") == '<p> this is a string </p>'
    assert string_five("foo") == '<p> foofoofoofoofoo </p>'
