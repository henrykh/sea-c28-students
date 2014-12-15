#!/usr/bin/env python

my_dict = {"name": "Chris", "city": "Seattle", "cake": "Chocolate"}
print my_dict

del my_dict["cake"]
print my_dict

my_dict["fruit"] = "mango"
print my_dict

print my_dict.keys()
print my_dict.values()
print "cake" in my_dict
print "mango" in my_dict.values()


x = range(16)
y = []
for number in range(16):
    y.append(chr(number).encode("hex"))

my_dict_2 = dict(zip(x, y))
print my_dict_2

my_dict_a = {}
for key in my_dict:
    my_dict_a[key] = my_dict[key].lower().count('a')
print my_dict_a

s2, s3, s4 = set(), set(), set()

for number in range(21):
    if number % 2 == 0:
        s2.add(number)
    if number % 3 == 0:
        s3.add(number)
    if number % 4 == 0:
        s4.add(number)

print s2
print s3
print s4

print s3.issubset(s2)
print s4.issubset(s2)

python_set = set('python')
python_set.add("i")
marathon_set = frozenset('marathon')
print python_set.union(marathon_set)
print python_set.intersection(marathon_set)
