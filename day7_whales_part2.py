#!/usr/bin/env python


"""Day 7: The Treachery of Whales. ALign crab submarines."""

import fileinput
import sys

def cost(n):
    return abs(n)*(abs(n)+1)/2

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: day7_whales_part2.py <input file>")
        sys.exit(-1)
    with open(sys.argv[1], 'r') as fin:
        positions = list(map(int, fin.readline().strip().split(',')))

    costs = [sum(map(lambda x:cost(x-target), positions)) for target in range(max(positions))]
    print(min(costs))
