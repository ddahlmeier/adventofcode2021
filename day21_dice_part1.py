#!/usr/bin/env python


"""--- Day 21: Dirac Dice ---"""


import sys


def deterministic_dice():
    dice=0
    while True:
        dice = dice%100
        dice+=1
        yield dice

def play(positions, score, dice):
    rolls = 0
    while True:
        for player in range(2):
            roll = [next(dice), next(dice), next(dice)]
            rolls += 3
            positions[player] = (((positions[player]+sum(roll))-1)%10)+1
            score[player] += positions[player]
            print("Player {} moves {} to space {} for total score {}".format(player+1, roll, positions[player], score[player]))
            if score[player]>=1000:
                return (positions, score, rolls)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: day21_dice_part1.py <input file>")
        sys.exit(-1)

    with open(sys.argv[1], 'r') as fin:
        positions = [int(fin.readline().split()[-1]), int(fin.readline().split()[-1])]

    score = [0, 0]
    dice = deterministic_dice()
    positions, score, rolls = play(positions, score, dice)
    print(min(score)*rolls)     
   