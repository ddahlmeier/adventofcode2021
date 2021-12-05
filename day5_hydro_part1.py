#!/usr/bin/env python


"""Hydrothermal venture. Avoid lines"""

from collections import defaultdict
import fileinput
import sys


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: day5_bingo_part1.py <input file>")
        sys.exit(-1)
    with open(sys.argv[1], 'r') as fin:
        lines = [tuple(tuple(map(int, point.split(',')))for point in line.split('->')) for line in fin]
    diagram = defaultdict(int)
    # map horizontal lines
    for line in lines:
        (x1, y1), (x2, y2) = line
        if x1==x2:
            y_small, y_large = (y1, y2) if y1<y2 else (y2,y1)
            for y in range(y_small, y_large+1):
                diagram[(x1, y)] += 1
        elif y1==y2:
            x_small, x_large = (x1, x2) if x1<x2 else (x2,x1)
            for x in range(x_small, x_large+1):
                diagram[(x, y1)] += 1
    # find dangeroud areas
    print(len(list(filter(lambda x: x[1]>=2, diagram.items()))))
    