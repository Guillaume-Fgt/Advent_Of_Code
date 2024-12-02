from collections import Counter

import aoc_lube

RAW = aoc_lube.fetch(year=2024, day=1)
# print(RAW)

def parse_raw():  # noqa: ANN201, D103
    first_col=[int(row.split()[0]) for row in RAW.split("\n")]
    second_col=[int(row.split()[1]) for row in RAW.split("\n")]
    first_col.sort()
    second_col.sort()
    return first_col,second_col


DATA = parse_raw()

def part_one():  # noqa: ANN201, D103
    differences=[abs(a-b) for a,b in zip(DATA[0],DATA[1])]
    return sum(differences)



def part_two():  # noqa: ANN201, D103
    second_col_count=Counter(DATA[1])
    sim_score=0
    for elem in DATA[0]:
        sim_score+=elem*second_col_count[elem]
    return sim_score


# aoc_lube.submit(year=2024, day=1, part=1, solution=part_one)
# aoc_lube.submit(year=2024, day=1, part=2, solution=part_two)
