#!/usr/bin/env python


def p_wrapper(func):
    def wrapped_string(string):
        return '<p> {} </p>'.format(func(string))
    return wrapped_string
