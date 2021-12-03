#!/usr/bin/env python


"""Compute diagnostic report from binary input. """

import fileinput
import sys


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: day3_diagnostic_part1.py <input file>")
        sys.exit(-1)
    report = [list(map(int, line.strip())) for line in fileinput.input(files=sys.argv[1])]
    pivot = list(zip(*report))
    gamma_rate = int("".join(['1' if one_count > len(report)/2 else '0' for one_count in map(sum, pivot)]), 2)
    epsilon_rate = int("".join(['0' if one_count > len(report)/2 else '1' for one_count in map(sum, pivot)]), 2)
    print(gamma_rate*epsilon_rate)