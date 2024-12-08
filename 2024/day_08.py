import itertools
from collections import defaultdict

import aoc_lube

RAW = aoc_lube.fetch(year=2024, day=8).splitlines()
# print(RAW)

with open("2024/example.txt") as f:
    example = f.read().splitlines()


def in_bounds(x, y, h, w):
    return 0 <= x < h and 0 <= y < w


def part_one():
    h, w = len(RAW), len(RAW[0])
    frequencies = defaultdict(list)
    for r in range(h):
        for c in range(w):
            if (char := RAW[r][c]) != ".":
                frequencies[char].append((r, c))
    antinodes = []
    for freq in frequencies.values():
        pair = itertools.combinations(freq, 2)
        for x, y in pair:
            diff = (y[0] - x[0], y[1] - x[1])
            if in_bounds(x[0] - diff[0], x[1] - diff[1], h, w):
                antinodes.append((x[0] - diff[0], x[1] - diff[1]))
            if in_bounds(y[0] + diff[0], y[1] + diff[1], h, w):
                antinodes.append((y[0] + diff[0], y[1] + diff[1]))
    return len(set(antinodes))

def part_two():
    h, w = len(RAW), len(RAW[0])
    frequencies = defaultdict(list)
    for r, c in itertools.product(range(h), range(w)):
        if (char := RAW[r][c]) != ".":
            frequencies[char].append((r, c))

    antinodes = []
    for freq in frequencies.values():
        pair = itertools.combinations(freq, 2)
        for x, y in pair:
            diff = (y[0] - x[0], y[1] - x[1])
            r, c = x[0], x[1]
            while 0 <= r < h and 0 <= c < w:
                antinodes.append((r, c))
                r -= diff[0]
                c -= diff[1]
            r, c = y[0], y[1]
            while 0 <= r < h and 0 <= c < w:
                antinodes.append((r, c))
                r += diff[0]
                c += diff[1]

    return len(set(antinodes))


print(part_two())

# aoc_lube.submit(year=2024, day=8, part=1, solution=part_one)
# aoc_lube.submit(year=2024, day=8, part=2, solution=part_two)
