#!/usr/bin/env python


"""--- Day 21: Dirac Dice ---"""

from collections import defaultdict
import sys


def play(position_p1, positions_p2):
    universes = defaultdict(int)
    wins = [0,0]
    universes[((0, 0), (position_p1, positions_p2), 0, 0, 0, 0)] = 1
    for score1 in range(22):
        for score2 in range(22):
            for position_p1 in range(1,11):
                for position_p2 in range(1,11):
                    for player in [0,1]:
                        for dice1 in [1,2,3]:
                            count = universes[((score1, score2), (position_p1, position_p2), 0, 0, 0, player)]
                            universes[((score1, score2), (position_p1, position_p2), dice1, 0, 0, player)] += count
                            for dice2 in [1,2,3]:
                                count = universes[((score1, score2), (position_p1, position_p2), dice1, 0, 0, player)]
                                universes[((score1, score2), (position_p1, position_p2), dice1, dice2, 0, player)] += count
                                for dice3 in [1,2,3]:
                                    count = universes[((score1, score2), (position_p1, position_p2), dice1, dice2, 0, player)]
                                    advance = dice1+dice2+dice3
                                    if player == 0:
                                        new_position = ((position_p1+advance-1)%10)+1
                                        new_score = score1+new_position
                                        if new_score >= 21:
                                            wins[0] += count
                                        else:
                                            universes[((new_score, score2), (new_position, position_p2), 0, 0, 0, 1)] += count
                                    elif player == 1:
                                        new_position = ((position_p2+advance-1)%10)+1
                                        new_score = score2+new_position
                                        if new_score >= 21:
                                            wins[1] += count
                                        else:
                                            universes[((score1, new_score), (position_p1, new_position), 0, 0, 0, 0)] += count
                                    else:
                                        raise("Unknown player id")
    return wins


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: day21_dice_part2.py <input file>")
        sys.exit(-1)

    with open(sys.argv[1], 'r') as fin:
        start1, start2 = [int(fin.readline().split()[-1]), int(fin.readline().split()[-1])]

    wins = play(start1, start2)
    print(wins)
    if wins[0]>wins[1]:
        print("Player 1 wins in more universes")
    elif wins[1]>wins[0]:
        print("Player 2 wins in more universes")
    else:
        print("Draw")
