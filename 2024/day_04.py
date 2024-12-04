import itertools
from collections import defaultdict

import aoc_lube

RAW = aoc_lube.fetch(year=2024, day=4)


with open("2024/example.txt") as f:
    EXAMPLE = f.read()


def groups(data, func):
    grouping = defaultdict(list)
    for y in range(len(data)):
        for x in range(len(data[y])):
            grouping[func(x, y)].append(data[y][x])
    return ["".join(x) for x in map(grouping.get, sorted(grouping))]


def part_one():
    lines = RAW.splitlines()

    cols = groups(lines, lambda x, _: x)
    rows = groups(lines, lambda _, y: y)
    fdiag = groups(lines, lambda x, y: x + y)
    bdiag = groups(lines, lambda x, y: x - y)

    col_forward = [x.count("XMAS") for x in cols]
    col_backward = [x.count("SAMX") for x in cols]
    row_forward = [x.count("XMAS") for x in rows]
    row_backward = [x.count("SAMX") for x in rows]
    fdiag_forward = [x.count("XMAS") for x in fdiag]
    fdiag_backward = [x.count("SAMX") for x in fdiag]
    bdiag_forward = [x.count("XMAS") for x in bdiag]
    bdiag_backward = [x.count("SAMX") for x in bdiag]
    return (
        sum(col_forward)
        + sum(col_backward)
        + sum(row_forward)
        + sum(row_backward)
        + sum(fdiag_forward)
        + sum(fdiag_backward)
        + sum(bdiag_forward)
        + sum(bdiag_backward)
    )

def part_two():
    lines = RAW.splitlines()
    max_row = len(lines[0])
    max_col = len(lines)
    total = 0
    for i, j in itertools.product(range(max_row), range(max_col)):
        if (letter := lines[i][j]) != "A":
            continue
        if (
            i - 1 in range(max_row)
            and j - 1 in range(max_col)
            and i + 1 in range(max_row)
            and j + 1 in range(max_col)
        ):
            fdiag1 = lines[i - 1][j - 1]
            fdiag2 = lines[i + 1][j + 1]
            bdiag1 = lines[i - 1][j + 1]
            bdiag2 = lines[i + 1][j - 1]
            if (
                "".join(sorted(fdiag1 + letter + fdiag2)) == "AMS"
                and "".join(sorted(bdiag1 + letter + bdiag2)) == "AMS"
            ):
                total += 1
    return total


aoc_lube.submit(year=2024, day=4, part=1, solution=part_one)
aoc_lube.submit(year=2024, day=4, part=2, solution=part_two)
