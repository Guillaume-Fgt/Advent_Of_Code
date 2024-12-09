import aoc_lube

games = [
    (ord(a) - ord("A"), ord(b) - ord("X"))
    for a, _, b in aoc_lube.fetch(year=2022, day=2).splitlines()
]

def part_one() -> int:
    return sum(b + 1 + 3 * ((b - a + 1) % 3) for a, b in games)

def part_two() -> int:
    return sum((b - 1 + a) % 3 + 1 + 3 * b for a, b in games)

aoc_lube.submit(year=2022, day=2, part=1, solution=part_one)
aoc_lube.submit(year=2022, day=2, part=2, solution=part_two)
print(part_one())
print(part_two())
