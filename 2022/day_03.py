import itertools

import aoc_lube

rucksacks = aoc_lube.fetch(year=2022, day=3).splitlines()

def priority(letter: str):
    return (
        1 + ord(letter) - ord("a")
        if letter.islower()
        else 1 + ord(letter) - ord("A") + 26
    )

def part_one():
    total = 0
    for rucksack in rucksacks:
        comp1, comp2 = (
            set(rucksack[: len(rucksack) // 2]),
            set(rucksack[len(rucksack) // 2 :]),
        )
        both = comp1 & comp2
        for x in both:
            total += priority(x)
    return total

def part_two():
    total = 0
    for group in itertools.batched(rucksacks, 3):
        r1, r2, r3 = group
        common = set(r1) & set(r2) & set(r3)
        for x in common:
            total += priority(x)
    return total


aoc_lube.submit(year=2022, day=3, part=1, solution=part_one)
aoc_lube.submit(year=2022, day=3, part=2, solution=part_two)
