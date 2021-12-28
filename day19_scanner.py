#!/usr/bin/env python


"""--- Day 19: Beacon Scanner ---"""


from collections import defaultdict
from itertools import permutations
import numpy as np
import sys


def read_scan(input):
    lines = input.splitlines()
    assert(lines[0].startswith("---"))
    scan = []
    for line in lines[1:]:
        scan.append(tuple(map(int, line.split(","))))
    return scan

def read_scans(fin):
    scans = list(map(read_scan, fin.read().strip().split("\n\n")))
    return scans

def generate_orientations(scan):
    for x in [1,-1]:
        for y in [1,-1]:
            for z in [1,-1]:
                for swap in permutations(range(3)):
                    rotation = np.eye(3)
                    rotation[:,0] = rotation[:,0]*x
                    rotation[:,1] = rotation[:,1]*y
                    rotation[:,2] = rotation[:,2]*z
                    rotation = rotation[:,swap]
                    rotated = [tuple(rotation.dot(np.array(vector))) for vector in scan]
                    yield (rotation, rotated)

def find_alignment(scan1, scan2, threshold=12):
    for point1 in scan1:
        for point2 in scan2:
            translation = np.array(point1)-np.array(point2)
            beacons = set(scan1).intersection({tuple(p) for p in np.array(scan2)+translation})
            if len(beacons) >= threshold:
                return (translation, beacons)
    return (None, None)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: day19_scanner_part1.py <input file>")
        sys.exit(-1)

    with open(sys.argv[1], 'r') as fin:
        scans = read_scans(fin)

    alignments = defaultdict(list)
    for scan1 in range(len(scans)):
        for scan2 in range(len(scans)):
            if scan1 == scan2:
                continue
            print("align scan", scan1, "and ", scan2)
            for rotation, rotated in generate_orientations(scans[scan2]):
                translation, beacons = find_alignment(scans[scan1], rotated)
                if translation is not None:
                    alignments[scan1].append((scan2, rotation, translation))
                    print("found overlap with rotation", rotation, "and translation", translation)
                    break
    # do depth first search in alignment tree and create set of all beacons
    beacons = set()
    visited = set()
    stack = [(0, np.array([0,0,0]), np.eye(3))]
    while len(stack)>0:
        scanner, position, rotation = stack.pop()
        visited.add(scanner)
        print("add beacons for scanner", scanner, "with position", position, "and rotation", rotation)
        for beacon in scans[scanner]:
            beacon = tuple(position + rotation.dot(np.array(beacon)))
            print("add beacon ", beacon)
            beacons.add(beacon)
        for next_scanner, next_rotation, next_translation in alignments[scanner]:
            if next_scanner not in visited:
                print("push scanner", next_scanner)
                stack.append((next_scanner, position + rotation.dot(next_translation), rotation.dot(next_rotation)))
    print(beacons)
    print(len(beacons))



