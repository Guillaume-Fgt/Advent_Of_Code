import itertools

import aoc_lube

RAW = aoc_lube.fetch(year=2024, day=7)


def can_obtain(target, array):
    if len(array) == 1:
        return target == array[0]
    if target % array[-1] == 0 and can_obtain(target // array[-1], array[:-1]):
        return True
    if target > array[-1] and can_obtain(target - array[-1], array[:-1]):
        return True
    if (
        len(str(target)) > len(str(array[-1]))
        and str(target).endswith(str(array[-1]))
        and can_obtain(int(str(target)[: -len(str(array[-1]))]), array[:-1])
    ):
        return True
    return False

def part_one():
    total = 0
    for line in RAW.splitlines():
        left, right = line.split(": ")
        target = int(left)
        array = [int(x) for x in right.split()]

        if can_obtain(target, array):
            total += target
    return total

def part_two():
    total = 0
    for line in RAW.splitlines():
        left, right = line.split(": ")
        target = int(left)
        array = [int(x) for x in right.split()]

        if can_obtain(target, array):
            total += target
    return total

print(part_one())
# aoc_lube.submit(year=2024, day=7, part=1, solution=part_one)
aoc_lube.submit(year=2024, day=7, part=2, solution=part_two)
