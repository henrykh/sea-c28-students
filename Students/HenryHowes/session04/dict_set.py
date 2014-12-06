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


x = []
y = "abcdefghijklmnop"
for number in range(16):
    x.append(number)


my_dict_2 = dict(zip(x, y))
print my_dict_2

my_dict_a = {}
for key in my_dict:
    a_count = 0
    for letter in my_dict[key]:
        if letter == "a" or letter == "A":
            a_count += 1
    my_dict_a[key] = a_count

print my_dict_a

s2, s3, s4 = set(), set(), set()

for number in range(21):
    s2.add(number/2)
    s3.add(number/3)
    s4.add(number/4)

print s2
print s3
print s4

print s3.issubset(s2)
print s4.issubset(s2)

python_set = {"p", "y", "t", "h", "o", "n"}
python_set.add("i")
marathon_set = frozenset(["m" , "a", "r", "a", "t", "h", "o", "n"])
print python_set.union(marathon_set)
print python_set.intersection(marathon_set)
