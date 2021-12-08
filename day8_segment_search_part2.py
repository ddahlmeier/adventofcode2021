#!/usr/bin/env python


"""Day 8: Seven Segment Search."""


from itertools import chain, permutations
import fileinput
import sys

"""
  0:      1:      2:      3:      4:
 aaaa    ....    aaaa    aaaa    ....
b    c  .    c  .    c  .    c  b    c
b    c  .    c  .    c  .    c  b    c
 ....    ....    dddd    dddd    dddd
e    f  .    f  e    .  .    f  .    f
e    f  .    f  e    .  .    f  .    f
 gggg    ....    gggg    gggg    ....

  5:      6:      7:      8:      9:
 aaaa    aaaa    aaaa    aaaa    aaaa
b    .  b    .  .    c  b    c  b    c
b    .  b    .  .    c  b    c  b    c
 dddd    dddd    ....    dddd    dddd
.    f  e    f  .    f  e    f  .    f
.    f  e    f  .    f  e    f  .    f
 gggg    gggg    ....    gggg    gggg

 """


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: day8_segment_search_part2.py <input file>")
        sys.exit(-1)

    segments = "abcdefg"
    digits = { "abcefg": "0",
                "cf": "1",
                "acdeg": "2",
                "acdfg": "3",
                "bcdf": "4",
                "abdfg": "5",
                "abdefg": "6",
                "acf": "7",
                "abcdefg": "8",
                "abcdfg": "9"}
  
   
    with open(sys.argv[1], 'r') as fin:
        result = 0
        for line in fin:
            signals, outputs = map(lambda x:x.split(), line.strip().split('|'))
            
            # search through all possibble permuations
            for permutation in permutations(segments):
                wiring = dict(zip(permutation, segments))
                possible_mapping = True
                for signal in signals:
                    # check if this digit is possible with this wiring
                    mapped = ''.join(sorted(map(lambda x: wiring[x], signal)))
                    if not mapped in digits.keys():
                        possible_mapping = False
                        break
                if possible_mapping:
                    value = int(''.join([digits[''.join(sorted(map(lambda x: wiring[x], output)))] for output in outputs]))
                    result += value
                    print(outputs, value)
        print(result)






