#!/usr/bin/env python


"""Day 14: Extended Polymerization"""

from collections import Counter
import sys

def parse_rules(rules):
    return dict(map(lambda x: tuple(x.split(' -> ')), rules.splitlines()))


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: day14_polymer_part1.py <input file>")
        sys.exit(-1)

    with open(sys.argv[1], 'r') as fin:
        template, rules = fin.read().split("\n\n")
    
    polymer = template
    rules = parse_rules(rules)
    for step in range(10):
        print(step)
        next_polymer = ""
        for i, char in enumerate(polymer):
            next_polymer += char
            if polymer[i:i+2] in rules.keys():
                next_polymer += rules[polymer[i:i+2]]
        polymer = next_polymer
    counts = sorted(Counter(polymer).items(), key=lambda x: x[1])
    print(sorted(counts))
    print(counts[-1][1] - counts[0][1])