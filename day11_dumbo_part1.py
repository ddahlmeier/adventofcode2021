#!/usr/bin/env python


"""Day 11: Dumbo Octopus"""

from collections import defaultdict
import sys

def increase_all(levels):
    for point in levels:
        levels[point] += 1

def increase_flashed(levels, flashing):
    for point in levels:
        for neighbor in neighbours(point):
            if flashing[neighbor]:
                levels[point] += 1

def reset_flashed(levels, has_flashed):
    for point in levels:
        if has_flashed[point]:
            levels[point] = 0

def calculate_flashing(levels, has_flashed):
    flashing = defaultdict(bool)
    for k, v in levels.items():
        flashing[k] = v>9 and not has_flashed[k]
    return flashing

def memorize_flashed(has_flashed, flashing):
    for point, flashed in flashing.items():
        if flashed:
            has_flashed[point] = True

def neighbours(point):
    for h, v in [(-1,-1), (-1,0), (-1,1), (0,-1), (0,1), (1,-1), (1,0), (1,1)]:
        yield((point[0]+h, point[1]+v))


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: day11_dumbo_part1.py <input file>")
        sys.exit(-1)

    with open(sys.argv[1], 'r') as fin:
        inputs = [list(map(int, line.strip())) for line in fin.readlines()]
    
    energy_levels = dict([((r,c), inputs[r][c]) for r in range(len(inputs)) for c in range(len(inputs[0]))])
    total_flashes = 0
    for step in range(100):
        has_flashed = defaultdict(bool)
        increase_all(energy_levels)
        flashing = calculate_flashing(energy_levels, has_flashed)
        increase_flashed(energy_levels, flashing)
        total_flashes += sum(flashing.values())
        memorize_flashed(has_flashed, flashing)  
        while any(flashing.values()):
            flashing = calculate_flashing(energy_levels, has_flashed)
            increase_flashed(energy_levels, flashing)
            total_flashes += sum(flashing.values())
            memorize_flashed(has_flashed, flashing)
        reset_flashed(energy_levels, has_flashed)
    print(total_flashes)
