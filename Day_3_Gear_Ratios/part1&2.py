import itertools
import math
import re
from collections import defaultdict

PUZZLE_FILENAME = "Day_3_Gear_Ratios/puzzle_input.txt"


def get_puzzle_lines() -> list[str]:
    with open(PUZZLE_FILENAME) as f:
        return f.readlines()


def main():
    lines = get_puzzle_lines()
    parts = defaultdict(list)
    special_chars = {
        (r, c)
        for r, c in itertools.product(range(len(lines)), range(len(lines)))
        if lines[r][c] not in "01234566789."
    }

    for index, line in enumerate(lines):
        for n in re.finditer(r"\d+", line):
            edge = {
                (r, c)
                for r in (index - 1, index, index + 1)
                for c in range(n.start() - 1, n.end() + 1)
            }
            for o in edge & special_chars:
                parts[o].append(int(n.group(0)))

    print(
        sum(sum(p) for p in parts.values()),
        sum(math.prod(p) for p in parts.values() if len(p) == 2),
    )


if __name__ == "__main__":
    main()
