import sys
from math import *
from time import *
from collections import *
from heapq import *


def part1(data):
    answer = 0
    for v in data:
        f = s = ''
        n = len(v)
        i = 0
        j = n - 1
        while not f or not s:
            if not f and v[i].isnumeric():
                f = v[i]
            if not s and v[j].isnumeric():
                s = v[j]
            i += 1
            j -= 1
        answer += int(f + s)
    return answer


def part2(data):
    nums = {
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9",
    }
    answer = 0
    for word in data:
        min_i = inf
        max_i = -1
        min_digit = max_digit = None
        for k, v in nums.items():
            if k in word:
                word_i = word.index(k)
                if word_i < min_i:
                    min_i = word_i
                    min_digit = nums[k]
                word_i = word.rindex(k)
                if word_i > max_i:
                    max_i = word_i
                    max_digit = nums[k]

            if v in word:
                digit_i = word.index(v)
                if digit_i < min_i:
                    min_i = digit_i
                    min_digit = v
                digit_i = word.rindex(v)
                if digit_i > max_i:
                    max_i = digit_i
                    max_digit = v
        answer += int(min_digit + max_digit)
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