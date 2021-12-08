#!/usr/bin/env python


"""Day 8: Seven Segment Search."""

from collections import Counter
import fileinput
import sys


def count(input):
    return Counter(map(len, input))

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: day8_segment_search_part1.py <input file>")
        sys.exit(-1)
    # mapping from digits to number of segments
    digits_segments = {0: 6, 1:2, 2:5, 3:5, 4:4, 5:5, 6:6, 7:3, 8:7, 9:6}

    counts = Counter()
    with open(sys.argv[1], 'r') as fin:
        for line in fin:
            signal, output = map(lambda x:x.split(), line.strip().split('|'))
            counts += count(output)
    result = sum([counts[digits_segments[d]] for d in [1, 4, 7, 8]])
    print(result)