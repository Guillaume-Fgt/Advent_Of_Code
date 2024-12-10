import itertools
from collections import defaultdict, deque

import aoc_lube

RAW = aoc_lube.fetch(year=2024, day=10).splitlines()


h, w = len(RAW), len(RAW[0])


def in_map(x: int, y: int) -> bool:  # noqa: D103
    return 0 <= x < h and 0 <= y < w


def get_neighbors(x: int, y: int):
    neighbors = []
    for point in [(x + 1, y), (x - 1, y), (x, y - 1), (x, y + 1)]:
        if in_map(*point):
            neighbors.append(point)
    return neighbors


def is_gradual(point1: tuple[int, int], point2: tuple[int, int]):
    x1, y1, x2, y2 = point1[0], point1[1], point2[0], point2[1]
    return int(RAW[x1][y1]) - int(RAW[x2][y2]) == 1

def part_one():
    trailheads = [
        (r, c) for r, c in itertools.product(range(h), range(w)) if int(RAW[r][c]) == 0
    ]

    trails = defaultdict(list)
    for trailhead in trailheads:
        steps = deque()
        steps.append(trailhead)
        visited = []
        while len(steps) > 0:
            new = steps.popleft()
            neighbors = get_neighbors(*new)
            for neighbor in neighbors:
                if is_gradual(neighbor, new) and neighbor not in visited:
                    visited.append(neighbor)
                    steps.append(neighbor)
                    trails[trailhead].append(int(RAW[neighbor[0]][neighbor[1]]))
    return sum([x.count(9) for x in trails.values()])


def part_two():
    trailheads = [
        (r, c) for r, c in itertools.product(range(h), range(w)) if int(RAW[r][c]) == 0
    ]

    trails = defaultdict(list)
    for trailhead in trailheads:
        steps = deque()
        steps.append(trailhead)
        while len(steps) > 0:
            new = steps.popleft()
            neighbors = get_neighbors(*new)
            for neighbor in neighbors:
                if is_gradual(neighbor, new):
                    steps.append(neighbor)
                    trails[trailhead].append(int(RAW[neighbor[0]][neighbor[1]]))
    return sum([x.count(9) for x in trails.values()])


aoc_lube.submit(year=2024, day=10, part=1, solution=part_one)
aoc_lube.submit(year=2024, day=10, part=2, solution=part_two)
