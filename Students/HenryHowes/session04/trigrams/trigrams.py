#!/usr/bin/env python

import io
import random

sherlock_file = io.open('sherlock_small.txt')
sherlock_text = sherlock_file.read()
sherlock_text = sherlock_text.replace('\n', " ").split(" ")


sherlock_trigrams = {}
for i, word in enumerate(sherlock_text):
    if i <= (len(sherlock_text)-3):
        sherlock_trigrams[word, sherlock_text[i+1]] = sherlock_text[i+2]

sherlock_output = open ("sherlock_output.txt", "w")
for number in range(50):
    random_key = random.choice(sherlock_trigrams.keys())
    print random_key
    random_trigram = "{a} {b} {c} ".format(a = random_key[0], b = random_key[1], c = sherlock_trigrams[random_key])
    sherlock_output.write(random_trigram)


sherlock_output.close()
sherlock_file.close()