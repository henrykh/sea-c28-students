#!/usr/bin/env python

import io

sherlock_file = io.open('sherlock_small.txt')
sherlock_text = sherlock_file.read()
sherlock_text = sherlock_text.split(" ")


sherlock_trigrams = {}
for i, word in enumerate(sherlock_text):
    if i <= (len(sherlock_text)-3):
        sherlock_trigrams[word, sherlock_text[i+1]] = sherlock_text[i+2]


print sherlock_trigrams
