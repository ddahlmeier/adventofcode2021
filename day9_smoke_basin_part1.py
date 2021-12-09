#!/usr/bin/env python


"""Day 9: Smoke Basin. Find low points in height map"""

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
        print("Usage: day9_smoke_basin_part1.py <input file>")
        sys.exit(-1)

    with open(sys.argv[1], 'r') as fin:
        hmap = [list(map(int, list(line.strip()))) for line in fin.readlines()]

    hmap_dim = (len(hmap), len(hmap[0]))
    lowpoint_sum = sum([hmap[r][c]+1 if is_lowpoint(hmap, r, c) else 0 for c in range(hmap_dim[1]) for r in range(hmap_dim[0])])
    print(lowpoint_sum)