import sys
from math import *
from time import *
from collections import *
from heapq import *


def part1(data):
    answer = 0
    for wins, nums in data:
        count = 0
        for num in nums:
            if num in wins:
                count += 1
        if count:
            answer += 2 ** (count - 1)
    return answer


def part2(data):
    copies = []
    for i, v in enumerate(data):
        wins, nums = v
        match = 0
        for num in nums:
            if num in wins:
                match += 1
        copy = 1
        for j, v in enumerate(copies):
            if i - j <= v[1]:
                copy += v[0]
        copies.append((copy, match))
    return sum([c[0] for c in copies])



if __name__ == "__main__":
    data = []
    with open(sys.argv[1], 'r') as f:
        for raw_line in f:
            line = raw_line.strip()
            if not line:
                break
            r0, r1 = line.split(' | ')
            r0 = r0.split(': ')[1]

            wins = set([int(r0[i:i+2]) for i in range(0, len(r0), 3)])
            nums = [int(r1[i:i+2]) for i in range(0, len(r1), 3)]

            data.append((wins, nums))

    if sys.argv[2] == "part1":
        print(f'Part 1 Answer = {part1(data)}')
    if sys.argv[2] == "part2":
        print(f'Part 2 Answer = {part2(data)}')