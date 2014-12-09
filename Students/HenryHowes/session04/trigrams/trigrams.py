#!/usr/bin/env python

import io
import random


sherlock_file = io.open('sherlock.txt')
sherlock_text = sherlock_file.read()
sherlock_text = sherlock_text.replace('\n', " ").split(" ")


sherlock_trigrams = {}
for i, word in enumerate(sherlock_text):
    if i < (len(sherlock_text)-2):
        first_two = (word, sherlock_text[i+1])
        if first_two not in sherlock_trigrams:
            sherlock_trigrams[first_two] = []
        sherlock_trigrams[first_two].append(sherlock_text[i+2])

sherlock_output = open("sherlock_output.txt", "w")

key = random.choice(sherlock_trigrams.keys())
sherlock_output.write("{a} {b}".format(a=key[0], b=key[1]))
for number in range(200):
    value = random.choice(sherlock_trigrams[key])
    sherlock_output.write(" {}".format(value))
    key = (key[1], value)
    if key not in sherlock_trigrams:
        key = random.choice(sherlock_trigrams.keys())


sherlock_output.close()
sherlock_file.close()
