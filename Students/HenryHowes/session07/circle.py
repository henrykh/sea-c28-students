#!/usr/bin/env python
"""circle class --

fill this in so it will pass all the tests.
"""
import math


class Circle(object):

    def __init__(self, radius):
        self._radius = radius

    def _getradius(self):
        return self._radius

    def _setradius(self, value):
        self._radius = value

    def _getdiameter(self):
        return self._radius*2

    def _setdiameter(self, value):
        self._radius = value / 2

    def _getarea(self):
        return (self._radius ** 2) * math.pi 

    def __str__(self):
        return 'Circle with radius: %0.6f' % self._radius  

    def __repr__(self):
        return "Circle({})".format(self.radius)

    def __add__(self, other):
        if isinstance(other, Circle):
            return Circle(self._radius + other.radius)
        else:
            return Circle(self._radius + other)

    def __mul__(self, other):
        if isinstance(other, Circle):
            return Circle(self._radius * other.radius)
        else:
            return Circle(self._radius * other)

    def __eq__(self, other):
        return (isinstance(other, self.__class__)) and self.radius == other.radius

    def __ne__(self, other):
        return not self.__eq__(other)

    def __gt__(self, other):
        return (isinstance(other, self.__class__)) and self.radius > other.radius

    def __lt__(self, other):
        return (isinstance(other, self.__class__)) and self.radius < other.radius

    def __ge__(self, other):
        return self.__eq__(other) or self.__gt__(other)

    def __le__(self, other):
        return self.__eq__(other) or self.__lt__(other)

    radius = property(_getradius, _setradius)
    diameter = property(_getdiameter, _setdiameter)
    area = property(_getarea)
