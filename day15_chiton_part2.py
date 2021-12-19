#!/usr/bin/env python


"""Day 15: Chiton"""

from operator import itemgetter
import heapq
import copy
import sys

def parse_risk(fin):
    risk_map = {}
    risk_input = fin.readlines()
    for y, row in enumerate(risk_input):
        for x, risk in enumerate(row.strip()):
            risk_map[(x,y)] = int(risk)
    return risk_map

def print_map(risk_map):
    for y in range(max(map(itemgetter(1), risk_map))+1):
        for x in range(max(map(itemgetter(0), risk_map))+1):
            print(risk_map[(x,y)], end="")
        print("")
    print("")

def expand_map(risk_map):
    full_map = copy.deepcopy(risk_map)
    dim_x = max(map(itemgetter(0), risk_map))+1
    dim_y = max(map(itemgetter(1), risk_map))+1
    for x in range(5*dim_x):
        for y in range(5*dim_y):
            if (x<dim_x and y<dim_y):
                continue
            full_map[(x,y)] = ((risk_map[(x%dim_x,y%dim_y)]+(x//dim_x)+(y//dim_y))-1) % 9 +1
    return full_map

def neighbors(point, map):
    for x,y in [(-1,0), (1,0), (0,-1), (0,1)]:
        if (point[0]+x, point[1]+y) in map.keys():
            yield (point[0]+x, point[1]+y)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: day15_chiton_part2.py <input file>")
        sys.exit(-1)

    with open(sys.argv[1], 'r') as fin:
        risk_map = parse_risk(fin)
    full_map = expand_map(risk_map)

    start = (0,0)
    target = max(full_map)
    heap =[(0, start)]
    shortest_path = dict([(point, float('inf')) for point in full_map.keys()])
    while True:
        risk, point = heapq.heappop(heap)
        if point == target:
            print("found shortest path with total risk: ", risk)
            break
        for neighbor in neighbors(point, full_map):
            risk_score = risk+full_map[neighbor]
            if risk_score < shortest_path[neighbor]:
                heapq.heappush(heap, (risk_score, neighbor))
                shortest_path[neighbor] = risk_score
