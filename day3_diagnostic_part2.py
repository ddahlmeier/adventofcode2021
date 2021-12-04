#!/usr/bin/env python


"""Compute diagnostic report from binary input."""

from operator import itemgetter, ge, lt
import fileinput
import sys

def bit_criteria(report, index, cmp):
    return 1 if cmp(sum(map(itemgetter(index), report)), len(report)/2) else 0

def generate_rating(report, rating="oxygen"):
    if rating == "oxygen":
        cmp = ge
    elif rating == "co2":
        cmp = lt
    else:
        sys.exit(1)

    for index in range(len(report)):
        bit = bit_criteria(report, index, cmp)   
        report = list(filter(lambda x: x[index] == bit, report))
        if len(report) == 1:
            break
    return int(''.join(map(str, report[0])),2)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: day3_diagnostic_part2.py <input file>")
        sys.exit(-1)
    report = [list(map(int, line.strip())) for line in fileinput.input(files=sys.argv[1])]
    oxygen_generator_reading = generate_rating(report, rating="oxygen")
    co2_scrubber_rating = generate_rating(report, rating="co2")
    print(oxygen_generator_reading*co2_scrubber_rating)