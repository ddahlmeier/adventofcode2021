#!/usr/bin/env python


""" Calculate the exponential growth of laternfish population efficiently."""

from collections import Counter
import sys


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: day6_lanternfish_part2.py <days> <input file>")
        sys.exit(-1)
    days = int(sys.argv[1])
    with open(sys.argv[2], 'r') as fin:
           state = Counter(map(int, fin.readline().strip().split(",")))
    for day in range(days):
        new_fish = state.get(0, 0)
        state = dict(filter(lambda x:x[0]>=0, map(lambda x: (x[0]-1,x[1]), state.items())))
        state[6] = state.get(6,0) + new_fish
        state[8] = new_fish
    print(sum(state.values()))