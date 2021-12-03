#!/usr/bin/env python


"""Execute a series of navigation commands. Determine final position. """


import fileinput
import sys


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: day2_dive_part1.py <command file>")
        sys.exit(-1)
    input_file = sys.argv[1]
    action = {"forward": lambda x, y: (y[0]+x, y[1]),
                "up": lambda x, y: (y[0], y[1]-x),
                "down": lambda x, y: (y[0], y[1]+x)}
    position = (0, 0)
    for line in fileinput.input(files=input_file):
        if len(line.split()) != 2:
            continue
        command, value = line.split()
        position = action[command](int(value), position)

    print(position[0] * position[1])
