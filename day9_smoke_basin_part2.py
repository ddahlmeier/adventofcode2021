#!/usr/bin/env python


"""Day 9: Smoke Basin. Find basins in height map"""

from operator import itemgetter, mul
from functools import reduce
import math
import sys

def is_lowpoint(hmap, row, col):
    if row>0 and hmap[row][col] >= hmap[row-1][col]:
        return False
    if col>0 and hmap[row][col] >= hmap[row][col-1]:
        return False
    if row<len(hmap)-1 and hmap[row][col] >= hmap[row+1][col]:
        return False
    if col<len(hmap[0])-1 and hmap[row][col] >= hmap[row][col+1]:
        return False
    return True    


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: day9_smoke_basin_part2.py <input file>")
        sys.exit(-1)

    with open(sys.argv[1], 'r') as fin:
        hmap = [list(map(int, list(line.strip()))) for line in fin.readlines()]

    hmap_dim = (len(hmap), len(hmap[0]))
    lowpoints  = [(r,c) for c in range(len(hmap[0])) for r in range(len(hmap)) if is_lowpoint(hmap, r, c)]
    basins = []
    for lowpoint in lowpoints:
        basin = []
        stack = [lowpoint]
        while len(stack) > 0:
            point = stack.pop()
            if point in basin:
                continue
            basin.append(point)
            row, col = point
            if row>0 and hmap[row][col] < hmap[row-1][col] and hmap[row-1][col] != 9:
                stack.append((row-1, col))
            if col>0 and hmap[row][col] < hmap[row][col-1] and hmap[row][col-1] != 9:
                stack.append((row, col-1))
            if row<len(hmap)-1 and hmap[row][col]<hmap[row+1][col] and hmap[row+1][col] != 9:
                stack.append((row+1, col))
            if col<len(hmap[0])-1 and hmap[row][col]<hmap[row][col+1] and hmap[row][col+1] != 9:
                stack.append((row, col+1))
        basins.append(basin)
    print(reduce(mul, sorted([len(basin) for basin in basins], reverse=True)[:3], 1))




