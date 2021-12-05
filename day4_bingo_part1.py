#!/usr/bin/env python


"""Play bingo."""

from collections import defaultdict
import fileinput
import sys


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: day4_bingo_part1.py <input file>")
        sys.exit(-1)
    with open(sys.argv[1], 'r') as fin:
        bingo_input = fin.read().split("\n\n")
    # parse input
    numbers = list(map(int, bingo_input[0].split(',')))
    boards = [list(map(lambda x: x.split(), board.splitlines())) for board in bingo_input[1:]]
    boards = [[list(map(int, row)) for row in board]for board in boards]
    
    # build index
    index = defaultdict(list)
    for b, board in enumerate(boards):
        for r, row in enumerate(board):
            for c, value in enumerate(row):
                index[value].append((b, r, c))
    # play bingo
    marked = [[[0 for _ in range(5)] for _ in range(5)] for _ in range(b+1)]
    for number in numbers:
        for b, r, c in index[number]:
            marked[b][r][c] = 1
            # check winner
            if sum(marked[b][r]) == 5 or sum([marked[b][x][c] for x in range(5)]) == 5:
                print("Board {} wins!".format(b++1))
                score = 0
                for _row in range(5):
                    for _col in range(5):
                        if marked[b][_row][_col] == 0:
                            score += boards[b][_row][_col]
                score *= number
                print(score)
                sys.exit(0)

