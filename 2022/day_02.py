import aoc_lube

RAW = aoc_lube.fetch(year=2022, day=2)
POINTS = {"X": 1, "Y": 2, "Z": 3}
WINS = {"C": "X", "B": "Z", "A": "Y"}
DRAWS = {"C": "Z", "B": "Y", "A": "X"}
LOSES = {"A": "Z", "C": "Y", "B": "X"}
# print(RAW)



def part_one():
    total = 0
    for line in RAW.splitlines():
        opp, me = line.split(" ")
        if (opp, me) in DRAWS.items():
            total += 3
        if (opp, me) in WINS.items():
            total += 6
        total += POINTS[me]
    return total

def part_two():
    total = 0
    for line in RAW.splitlines():
        opp, result = line.split(" ")
        if result == "Y":
            total += POINTS[DRAWS.get(opp)] + 3
        if result == "X":
            total += POINTS[LOSES.get(opp)]
        if result == "Z":
            total += POINTS[WINS.get(opp)] + 6
    return total


aoc_lube.submit(year=2022, day=2, part=1, solution=part_one)
aoc_lube.submit(year=2022, day=2, part=2, solution=part_two)
