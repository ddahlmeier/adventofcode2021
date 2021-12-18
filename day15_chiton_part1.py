#!/usr/bin/env python


"""Day 15: Chiton"""

import heapq
import sys

def parse_risk(fin):
    risk_map = {}
    risk_input = fin.readlines()
    for x, row in enumerate(risk_input):
        for y, risk in enumerate(row.strip()):
            risk_map[(x,y)] = int(risk)
    return risk_map

def neighbors(point, map):
    for x,y in [(-1,0), (1,0), (0,-1), (0,1)]:
        if (point[0]+x, point[1]+y) in map.keys():
            yield (point[0]+x, point[1]+y)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: day15_chiton_part1.py <input file>")
        sys.exit(-1)

    with open(sys.argv[1], 'r') as fin:
        risk_map = parse_risk(fin)
    start = (0,0)
    target = max(risk_map)
    heap =[(0, start)]
    shortest_path = dict([(point, float('inf')) for point in risk_map.keys()])
    while True:
        risk, point = heapq.heappop(heap)
        if point == target:
            print("found shortest path with total risk: ", risk)
            break
        for neighbor in neighbors(point, risk_map):
            risk_score = risk+risk_map[neighbor]
            if risk_score < shortest_path[neighbor]:
                heapq.heappush(heap, (risk_score, neighbor))
                shortest_path[neighbor] = risk_score
