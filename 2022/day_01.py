import heapq

import aoc_lube

RAW = aoc_lube.fetch(year=2022, day=1)


def parse_raw() -> list[list[int]]:
    return [list(map(int, chunk.splitlines())) for chunk in RAW.split("\n\n")]


DATA = parse_raw()


def part_one() -> int:
    return max([sum(cals) for cals in DATA])


def part_two() -> int:
    return sum(heapq.nlargest(3, [sum(cals) for cals in DATA]))


aoc_lube.submit(year=2022, day=1, part=1, solution=part_one)
aoc_lube.submit(year=2022, day=1, part=2, solution=part_two)
