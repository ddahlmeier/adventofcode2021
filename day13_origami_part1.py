#!/usr/bin/env python


"""Day 13: Transparent Origami"""

from collections import defaultdict
from operator import itemgetter
import sys

def parse_instruction(inst):
    dim, value = inst.lstrip("fold along ").split('=')
    return dim, int(value)

def unique(_list):
    return list(set(_list))

def print_paper(points):
    get_x = itemgetter(0)
    get_y = itemgetter(1)
    for y in range(max(map(get_y, points))+1):
        for x in range(max(map(get_x, points))+1):
            if (x, y) in points:
                print('#', end="")
            else:
                print('.', end="")
        print("")
    print("")

def fold_paper(points, direction, position):
    if direction == "y":
        for x, y in points:
            if y <= position:
                yield (x, y)
            else:
                yield (x, 2*position-y)
    elif direction == "x":
        for x, y in points:
            if x <= position:
                yield (x, y)
            else:
                yield (2*position-x, y)
        pass
    else:
        print("unknown direction")
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: day13_origami_part1.py <input file>")
        sys.exit(-1)

    with open(sys.argv[1], 'r') as fin:
        points, instructions = fin.read().split("\n\n")
    
    points = list(map(lambda x: tuple(map(int, x.split(','))), points.splitlines()))
    instructions = list(map(parse_instruction, instructions.splitlines()))
    for direction, position in instructions:
        points = unique(fold_paper(points, direction, position))
    print_paper(points)
    