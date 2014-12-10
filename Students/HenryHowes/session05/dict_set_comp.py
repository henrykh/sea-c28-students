#!/usr/bin/env python

import string

food_prefs = {u"name": u"Henry", u"city": u"Seattle",u"pie": u"apple", u"fruit": u"mango",u"salad": u"pear balsamic", u"pasta": "gnocchi"}
print "{name} is from {city}, and he likes {pie}, {fruit}, {salad}, and {pasta}.".format(**food_prefs)

alpha_num_15 = {x: y for x, y in zip(range(16), string.lowercase[:16])}
print alpha_num_15

food_prefs_two = {x: y.count('a') for x, y in food_prefs.items()}
print food_prefs_two

s2 = {x for x in range(21) if x % 2 == 0}
s3 = {y for y in range(21) if y % 3 == 0}
s4 = {z for z in range(21) if z % 4 == 0}

def divisible_set_maker(number=3, number_range=20):
    """return the given number of sets of divisible numbers

       Keyword arguments:
       number -- the number of sets to be returned, defaults to 3
       number_range -- the range in which to look for divisible numbers
       """

    set_container = []
    for divisor in range (2, 2+number):
        print divisor
        set_container.append({n for n in range(number_range+1) if n % divisor == 0})

    return set_container


if __name__ == '__main__':
    print s2 
    print s3
    print s4

    print "set_maker_test"
    print divisible_set_maker()