#!/usr/bin/env python

# Hadoop_MapReduce_WordCounter
# Writing a Mapper Function to read in data from STDIN and STDOUT tuples of the form (word, 1)

import sys

for line in sys.stdin:

    line = line.strip()

    words = line.split()

    for word in words:

        print("{}\t{}".format(word,1))
