#!/usr/bin/env python


"""Execute a series of navigation commands. Determine final position. """


import fileinput
import sys


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: day2_dive_part1.py <command file>")
        sys.exit(-1)
    input_file = sys.argv[1]
    position = [0, 0]
    for line in fileinput.input(files=input_file):
    	if len(line.split()) != 2:
    		continue
    	command, value = line.split()
    	value = int(value)
    	if command == "forward":
    		position[0] += value
    	elif command == "up":
    		position[1] -= value
    	elif command == "down":
    		position[1] += value
    	else:
    		print("Unknown command {}", command)
    print(position[0] * position[1])
