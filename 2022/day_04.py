from typing import NamedTuple

import aoc_lube


class Assignement(NamedTuple):
    num_sec1: int
    num_sec2: int


def is_fully_contained(a: Assignement, b: Assignement) -> bool:
    set_a = set(range(a.num_sec1, a.num_sec2 + 1))
    set_b = set(range(b.num_sec1, b.num_sec2 + 1))
    return set_a.issubset(set_b) or set_b.issubset(set_a)


def overlap(a: Assignement, b: Assignement) -> bool:
    set_a = set(range(a.num_sec1, a.num_sec2 + 1))
    set_b = set(range(b.num_sec1, b.num_sec2 + 1))
    return not set_a.isdisjoint(set_b)


pairs = [x.split(",") for x in aoc_lube.fetch(year=2022, day=4).splitlines()]
assigns = [
    (Assignement(*map(int, x.split("-"))), Assignement(*map(int, y.split("-"))))
    for x, y in pairs
]



def part_one():
    return sum(
        [1 for assign1, assign2 in assigns if is_fully_contained(assign1, assign2)],
    )


def part_two():
    return sum(
        [1 for assign1, assign2 in assigns if overlap(assign1, assign2)],
    )


aoc_lube.submit(year=2022, day=4, part=1, solution=part_one)
aoc_lube.submit(year=2022, day=4, part=2, solution=part_two)
