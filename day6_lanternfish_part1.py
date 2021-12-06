#!/usr/bin/env python


""" Calculate the exponential growth of laternfish population."""

import sys


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: day6_lanternfish_part1.py <days> <input file>")
        sys.exit(-1)
    days = int(sys.argv[1])
    with open(sys.argv[2], 'r') as fin:
           state = list(map(int, fin.readline().strip().split(",")))
    for day in range(days):
        print(day)
        new_fish = state.count(0)
        state = list(map(lambda x: x-1 if x>0 else 6, state))
        state += [8]*new_fish
    print(len(state))
