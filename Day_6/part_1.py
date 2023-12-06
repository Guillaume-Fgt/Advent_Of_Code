import functools
import operator
import re
from pathlib import Path
from time import perf_counter

PUZZLE_FILENAME = "Day_6/puzzle_input.txt"


def get_puzzle_lines() -> list[str]:
    with Path(PUZZLE_FILENAME).open("r") as f:
        return f.readlines()


def main() -> None:
    time1 = perf_counter()
    lines = get_puzzle_lines()
    data = tuple(
        (
            zip(
                map(int, re.findall(r"\d+", lines[0])),
                map(int, re.findall(r"\d+", lines[1])),
            )
        ),
    )
    wins = []
    for time, distance in data:
        win_race = 0
        for hold in range(time // 2):
            if (time - hold) * hold > distance:
                win_race = (time + 1) - hold * 2
                break
        wins.append(win_race)

    print(functools.reduce(operator.mul, wins))
    print(f"time elapsed: {perf_counter()-time1}")


if __name__ == "__main__":
    main()
