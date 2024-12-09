import itertools
from collections import Counter

import aoc_lube

RAW = aoc_lube.fetch(year=2024, day=9)

example1 = "12345"
example2 = "2333133121414131402"


def calculate_checksum(str_map):
    return sum([i * int(v) for i, v in enumerate(str_map) if v != "."])


def part_one(disk_map):
    disk = []
    fid = 0

    for i, char in enumerate(disk_map):
        x = int(char)
        if i % 2 == 0:
            disk += [fid] * x
            fid += 1
        else:
            disk += [-1] * x

    blanks = [i for i, x in enumerate(disk) if x == -1]

    for i in blanks:
        while disk[-1] == -1:
            disk.pop()
        if len(disk) <= i:
            break
        disk[i] = disk.pop()
    return calculate_checksum(disk)


def part_two(disk_map):
    files = {}
    blanks = []
    pos = 0
    fid = 0
    for i, char in enumerate(disk_map):
        x = int(char)
        if i % 2 == 0:
            if x == 0:
                raise ValueError("unexpected x=0 for file")
            files[fid] = (pos, x)
            fid += 1
        elif x != 0:
            blanks.append((pos, x))
        pos += x

    while fid > 0:
        fid -= 1
        pos, size = files[fid]

        for i, (start, length) in enumerate(blanks):
            if start >= pos:
                blanks = blanks[:i]
                break
            if size <= length:
                files[fid] = (start, size)
                if size == length:
                    blanks.pop(i)
                else:
                    blanks[i] = (start + size, length - size)
                break

    total = 0
    for fid, (pos, size) in files.items():
        for x in range(pos, pos + size):
            total += fid * x
    return total

def solution():
    return part_one(RAW)

def solution2():
    return part_two(RAW)


aoc_lube.submit(year=2024, day=9, part=1, solution=solution)
aoc_lube.submit(year=2024, day=9, part=2, solution=solution2)
