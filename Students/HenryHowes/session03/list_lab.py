#!/usr/bin/env python

print u"Series One\n"
shopping_list = ["Apples","Pears","Oranges","Peaches"]
print shopping_list

new_item = raw_input(u"Please name another fruit to be added to this list : ")
shopping_list.append(new_item)
print shopping_list

user_number = int(raw_input(u"Please enter a number to display the fruit at that list position : "))
while(user_number < 1 or user_number > len(shopping_list)):
    print(u"List contains {length} items. Number must be between 1 and {length}".format(length=len(shopping_list)))
    user_number = int(raw_input(u"Please enter a number to display the fruit at that list position : "))

print u"{number} : {fruit}".format(number= user_number, fruit= shopping_list[user_number-1])

shopping_list = ["kiwi"] + shopping_list
print shopping_list

shopping_list.insert(0, "papaya")
print shopping_list

for fruit in shopping_list:
    if fruit.startswith('p') or fruit.startswith('P'):
        print fruit, 

print "\n"
print u"Series Two\n"

series_two_list = shopping_list[:]
print series_two_list
del series_two_list[-1]
print series_two_list

fruit_to_delete = raw_input(u"Name a fruit to remove from the list: ")
series_two_list *= 2
while fruit_to_delete not in series_two_list:
    print u"Fruit not found. Fruit in the list are {}".format(series_two_list)
    fruit_to_delete = raw_input(u"Please enter another fruit: ")
while fruit_to_delete in series_two_list:
    series_two_list.remove(fruit_to_delete)

print series_two_list


print "\n"
print u"Series Three\n"

series_three_list = shopping_list[:]
for fruit in series_three_list[:]:
    user_response = raw_input(u"Do you like {}? ".format(fruit.lower())).lower()
    while(user_response != "no" and user_response != "yes"):
        user_response = raw_input(u"Answer must be yes or no: ").lower()
    if user_response == "no" :
        series_three_list.remove(fruit)
print series_three_list

print "\n"
print u"Series Four\n"

series_four_list = shopping_list[:]
for index, fruit in enumerate(series_four_list):
    series_four_list[index] = fruit[::-1]
del shopping_list[-1]

print shopping_list
print series_four_list
