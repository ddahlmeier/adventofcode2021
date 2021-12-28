#!/usr/bin/env python


"""--- Day 20: Trench Map ---"""


import numpy as np
import sys


def convert(line):
    pixel = {"#": 1, ".": 0} 
    return [pixel[s] for s in line]

def print_map(image):
    for row in range(image.shape[0]):
        print(''.join(["#" if pixel == 1 else "." for pixel in image[row,:]]))
    print("")


def enhance(image, algorithm, background=0):
    pixel = {"#": 1, ".": 0}
    image = np.pad(image, 4, "constant", constant_values=(background,))
    padded = np.pad(image, 1, "constant", constant_values=(background,))
    enhanced = np.zeros(image.shape)

    for row in range(image.shape[0]):
        for col in range(image.shape[1]):
            window = padded[row:row+3,col:col+3]
            index = int(''.join((str(int(x)) for x in window.reshape(9,))), base=2)
            enhanced[row,col] = pixel[algorithm[index]]
    return enhanced




if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: day20_map_part1.py <input file>")
        sys.exit(-1)

    with open(sys.argv[1], 'r') as fin:
        algorithm = fin.readline().strip()
        fin.readline()
        image = np.array([convert(line.strip()) for line in fin.readlines()])
        background = 0
        for step in range(50):
            if algorithm[0] == '#':
                if step%2==1:
                    background=1
                else:
                    background=0
            image = enhance(image, algorithm, background=background)
        print(int(sum(sum(image))))
   