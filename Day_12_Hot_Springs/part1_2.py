import itertools
from pathlib import Path

PUZZLE_FILENAME = "Day_12_Hot_Springs/example.txt"


def get_puzzle_lines() -> list[str]:
    with Path(PUZZLE_FILENAME).open("r") as f:
        return f.read().splitlines()


def main() -> None:
    grid = get_puzzle_lines()
    r = (r.split() for r in grid)
    for c, g in r:
        total_hash = sum(map(int, g.split(",")))
        hash_in_string = c.count("#")
        question_in_string = c.count("?")
        hash_to_place = total_hash - hash_in_string
        combs = itertools.permutations(
            (question_in_string - hash_to_place) * "." + hash_to_place * "#",
            question_in_string,
        )
        print(list(combs))
        input()
    # print(list(itertools.permutations("###..", 5)))


if __name__ == "__main__":
    main()
