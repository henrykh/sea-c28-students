#!/usr/bin/env python

import sys


def trim_line(line):
    return ("{}".format(line.lstrip().rstrip()))

try:
    filename = sys.argv[1]
except IndexError:
    filename = ""
    while filename[-4:] != u".txt":
        filename = raw_input(
            u"Choose a file to remove leading and trailing whitespace from"
            "(must end with .txt): ")

the_file = open("{}".format(filename))
trimmed_lines = [trim_line(line) for line in the_file]
the_file.close()

answer = None
while answer != u"create new file" and answer != u"overwrite":
    answer = raw_input(u"Choose one: 'create new file' or 'overwrite' ")

if answer == "create new file":
    outputfilename = ""
    while outputfilename[-4:] != u".txt":
        outputfilename = raw_input(
            u"Choose a new file name (must end with .txt): ")
else:
    outputfilename = filename

output_file = open("{}".format(outputfilename), "w")
for line in trimmed_lines:
    output_file.write(u"{}\n".format(line))

output_file.close()
