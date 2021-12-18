#!/usr/bin/env python


"""Day 14: Extended Polymerization"""

from collections import defaultdict
import copy
import sys

def parse_rules(rules):
    return dict(map(lambda x: tuple(x.split(' -> ')), rules.splitlines()))

def parse_template(template):
    polymer = defaultdict(int)
    for i in range(len(template)-1):
        polymer[template[i:i+2]] += 1
    return polymer

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: day14_polymer_part1.py <input file>")
        sys.exit(-1)

    with open(sys.argv[1], 'r') as fin:
        template, rules = fin.read().split("\n\n")
    
    polymer = parse_template(template)
    rules = parse_rules(rules)
   
    for step in range(40):
        next_polymer = copy.deepcopy(polymer)
        for pattern, count in polymer.items():
            if pattern in rules.keys():
                next_polymer[pattern] -= count
                inserted = rules[pattern]
                next_polymer[pattern[0]+inserted] += count
                next_polymer[inserted+pattern[1]] += count
        polymer = next_polymer
    counts = defaultdict(int)
    for pattern, count in polymer.items():
        counts[pattern[0]] += count
    counts[template[-1]] += 1
    counts = sorted(counts.items(), key=lambda x: x[1])
    print(counts[-1][1] - counts[0][1])