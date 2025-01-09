import sys
from math import *
from time import *
from collections import *
from heapq import *
from re import *


def part1(data):
    answer = 0
    m = len(data)
    n = len(data[0])
    for i, line in enumerate(data):
        for match in finditer('\d+', line):
            isvalid = False
            start = match.start()
            end = match.end()

            if start > 0:
                left = line[start - 1]
                if left != '.':
                    isvalid = True
            if end < n:
                right = line[end]
                if right != '.':
                    isvalid = True

            if not isvalid:
                for j in range(start - 1, end + 1):
                    if j > - 1 and j < n:
                        if i > 0:
                            top = data[i - 1][j]
                            if not top.isdigit() and top != '.':
                                isvalid = True
                                break
                        if i < m - 1:
                            bottom = data[i + 1][j]
                            if not bottom.isdigit() and bottom != '.':
                                isvalid = True
                                break
            print(f'{i} {start} {end} {match.group()} {isvalid}')
            if isvalid:
                answer += int(match.group())
    return answer


def part2(data):
    answer = 0
    m = len(data)
    n = len(data[0])

    gears = {}
    for i in range(m):
        for j in range(n):
            if data[i][j] == '*':
                gears[(i, j)] = []

    for i, line in enumerate(data):
        for match in finditer('\d+', line):
            start = match.start()
            end = match.end()
            num = int(match.group())

            if (i, start - 1) in gears:
                gears[(i, start - 1)].append(num)
            if (i, end) in gears:
                gears[(i, end)].append(num)

            for j in range(start - 1, end + 1):
                if (i - 1, j) in gears:
                    gears[(i - 1, j)].append(num)
                if (i + 1, j) in gears:
                    gears[(i + 1, j)].append(num)
    for gear, parts in gears.items():
        if len(parts) == 2:
            answer += parts[0] * parts[1]
        else:
            print(f'{gear} {parts}')
    return answer


if __name__ == "__main__":
    data = []
    with open(sys.argv[1], 'r') as f:
        for raw_line in f:
            line = raw_line.strip()
            if not line:
                break
            data.append(line)

    if sys.argv[2] == "part1":
        print(f'Part 1 Answer = {part1(data)}')
    if sys.argv[2] == "part2":
        print(f'Part 2 Answer = {part2(data)}')