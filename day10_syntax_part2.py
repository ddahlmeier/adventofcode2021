#!/usr/bin/env python


"""Day 10: Syntax Scoring"""

import sys

def is_opening(symbol):
    return symbol in "([{<"

def is_closing(symbol):
    return symbol in ")]}>"

def matches(s1, s2):
    return (s1 == '(' and s2 == ')') or (s1 == '[' and s2 == ']') or (s1 == '{' and s2 == '}') or (s1 == '<' and s2 == '>') 

counterpart = {'(':')', '{':'}', '[':']', '<':'>'}
points = {')': 1, ']': 2, '}': 3, '>': 4}


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: day10_syntax_part2.py <input file>")
        sys.exit(-1)

    with open(sys.argv[1], 'r') as fin:
        lines = [line.strip() for line in fin.readlines()]
    scores = []
    for line in lines:
        stack = []
        is_corrupted = False
        for symbol in line:
            if is_opening(symbol):
                stack.append(symbol)
            elif is_closing(symbol):
                s_open = stack.pop()
                if not matches(s_open, symbol):
                    is_corrupted = True
                    break
            else:
                print("unknown symbol")
                sys.exit(1)
        if is_corrupted:
            continue
        stack.reverse()
        score = 0
        for symbol in stack:
            score *= 5
            score += points[counterpart[symbol]]
        print(line, score)
        scores.append(score)
    scores.sort()
    print(scores[len(scores)//2])
