import sys
from math import *
from time import *
from collections import *
from heapq import *
from functools import *
import operator


def part1(data, maxColors = {'red': 12, 'green': 13, 'blue': 14}):
    answer = 0
    for game in data:
        valid = True
        for gSet in game[1]:
            for color, count in gSet.items():
                if count > maxColors[color]:
                    valid = False
                    break
            if not valid:
                break
        if valid:
            answer += game[0]
    return answer


def part2(data):
    answer = 0
    for game in data:
        minColors = {}
        for gSet in game[1]:
            for color, count in gSet.items():
                if color in minColors:
                    minColors[color] = max(minColors[color], count)
                else:
                    minColors[color] = count
        answer += reduce(operator.mul, minColors.values())
    return answer

if __name__ == "__main__":
    data = []
    with open(sys.argv[1], 'r') as f:
        for raw_line in f:
            line = raw_line.strip()
            if not line:
                break
            gStr, cStr = line.split(': ')
            g = int(gStr.split(' ')[1])
            setsStr = cStr.split('; ')
            sets = []
            for s in setsStr:
                colorMap = {}
                for colors in s.split(', '):
                    count, color = colors.split(' ')
                    colorMap[color] = int(count)
                sets.append(colorMap)
            data.append((g, sets))

    if sys.argv[2] == "part1":
        print(f'Part 1 Answer = {part1(data)}')
    if sys.argv[2] == "part2":
        print(f'Part 2 Answer = {part2(data)}')