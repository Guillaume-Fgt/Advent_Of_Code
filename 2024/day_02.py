import aoc_lube

RAW = aoc_lube.fetch(year=2024, day=2)

def parse_raw():
    return [list(map(int,line.split())) for line in RAW.splitlines()]

DATA = parse_raw()
print(DATA)

def safe(row):
    return all(a<b and 1<=abs(a-b)<=3 for a,b in zip(row,row[1:])) or all(a>b and 1<=abs(a-b)<=3 for a,b in zip(row,row[1:]))

def all_decreasing(row):
    return all(a>b and 1<=abs(a-b)<=3 for a,b in zip(row,row[1:]))

def part_one():
    safe_reports=0
    for row in DATA:
        if safe(row):
            safe_reports+=1
    return safe_reports

def part_two():
    safe_reports=0
    for row in DATA:
        if any(safe(row[:i]+row[i+1:]) for i in range(len(row))):
                safe_reports+=1
    return safe_reports


aoc_lube.submit(year=2024, day=2, part=1, solution=part_one)
aoc_lube.submit(year=2024, day=2, part=2, solution=part_two)
