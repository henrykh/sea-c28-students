#!/usr/bin/env python

from rot13 import rot13
import string


def test_rot13_encoding():
    first_half_of_alphabet, second_half_of_alphabet = string.lowercase[:13], string.lowercase[13:27]
    assert rot13(u"test") == u"grfg"
    assert rot13(first_half_of_alphabet) == second_half_of_alphabet


def test_rot13_caps_preservation():
    assert rot13(u"TeSt") == u"GrFg"


def test_rot13_nonalpha_preservation():
    assert rot13(u"Here: a string that's full 2 the brim of non-@lphas") == u"Urer: n fgevat gung'f shyy 2 gur oevz bs aba-@ycunf"
