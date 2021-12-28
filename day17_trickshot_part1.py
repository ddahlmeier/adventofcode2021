#!/usr/bin/env python


"""---- Day 17: Trick Shot -----"""


import sys


def in_target(x, y, xtarget, ytarget):
    return True if x >= xtarget[0] and x <= xtarget[1] and y <= ytarget[1] and y >= ytarget[0] else False


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: day17_trickshot_part1.py <input file>")
        sys.exit(-1)

    with open(sys.argv[1], 'r') as fin:
        _, _, xtarget, ytarget = fin.readline().split()
    xtarget = tuple(map(int, xtarget.lstrip("x=").rstrip(",").split("..")))
    ytarget = tuple(map(int, ytarget.lstrip("y=").split("..")))
    highest_y = 0
    valid_count = 0
    for vx_start in range(1,216):
        for vy_start in range(-132, 10000):
            highest_y_local = -10
            x, y = 0, 0
            vx, vy = vx_start, vy_start
            for step in range(100000):
                x += vx
                y += vy
                highest_y_local = max(y, highest_y_local)
                if vx > 0:
                    vx -= 1
                elif vx <0:
                    vx += 1
                vy -= 1
                if in_target(x, y, xtarget, ytarget):
                    highest_y = max(highest_y, highest_y_local)
                    valid_count += 1
                    break
                if y < ytarget[0] or x > xtarget[1] or (vx==0 and (x<xtarget[0] or x>xtarget[1])):
                    break
    print(highest_y, valid_count)

    