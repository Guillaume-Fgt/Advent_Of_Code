import itertools
import math
import re
from collections import defaultdict

PUZZLE_FILENAME = "Day_3_Gear_Ratios/puzzle_input.txt"


def get_puzzle_lines() -> list[str]:
    with open(PUZZLE_FILENAME) as f:
        return f.readlines()


def get_special_chars(lines: list[str]) -> set[tuple[int, int]]:
    """returns the coordinate of all special characters inside the puzzle as a set"""
    num_lines = len(lines)
    length_line = len(lines[0])  # we assume all lines have same length
    return {
        (r, c)
        for r, c in itertools.product(range(num_lines), range(length_line))
        if lines[r][c] not in "01234566789.\n"
    }


def get_edge_num(index: int, n: re.Match) -> set[tuple[int, int]]:
    """given an line index and matched number, returns the content of char around num in a set"""
    return set(
        itertools.product(
            (index - 1, index, index + 1),
            range(n.start() - 1, n.end() + 1),
        ),
    )


def main() -> None:
    lines = get_puzzle_lines()
    parts = defaultdict(list)
    special_chars = get_special_chars(lines)

    for index, line in enumerate(lines):
        for n in re.finditer(r"\d+", line):
            edge = get_edge_num(index, n)
            for o in edge & special_chars:
                parts[o].append(int(n.group(0)))

    print(
        sum(sum(p) for p in parts.values()),
        sum(math.prod(p) for p in parts.values() if len(p) == 2),
    )


if __name__ == "__main__":
    main()
