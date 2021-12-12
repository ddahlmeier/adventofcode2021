#!/usr/bin/env python


"""Day 12: Passage Pathing """

from collections import defaultdict
import sys

def is_small_cave(cave):
    return cave.islower()

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: day12_passage_part1.py <input file>")
        sys.exit(-1)

    cavemap = defaultdict(list)
    with open(sys.argv[1], 'r') as fin:
        for line in fin.readlines():
            cave1, cave2 = line.strip().split("-")
            cavemap[cave1].append(cave2)
            cavemap[cave2].append(cave1)
    stack = [["start"]]
    valid_paths = 0
    while(len(stack) > 0):
        path = stack.pop()
        cave = path[-1]
        if cave == "end":
            valid_paths += 1
            print(path)
            continue
        for next_cave in cavemap[cave]:
            if is_small_cave(next_cave) and next_cave in path:
                continue
            stack.append(path + [next_cave])
    print(valid_paths)