import re
from itertools import starmap
from operator import mul

import aoc_lube

PATTERN1=r"mul\((\d+),(\d+)\)"
PATTERN2=r"mul\((\d+),(\d+)\)|(don't\(\))|(do\(\))"

RAW = aoc_lube.fetch(year=2024, day=3)


def process(a:str,b:str):
    return mul(int(a),int(b))


def part_one():
    m=re.findall(PATTERN1,RAW)
    product=starmap(process,m)
    return sum(product)


def part_two():
    m=re.findall(PATTERN2,RAW)
    enabled=True
    total=0
    for a,b,dont,do in m:
        if dont:
            enabled=False
            continue
        if do:
            enabled=True
            continue
        if enabled:
            total+=int(a)*int(b)
    return total

aoc_lube.submit(year=2024, day=3, part=1, solution=part_one)
aoc_lube.submit(year=2024, day=3, part=2, solution=part_two)
