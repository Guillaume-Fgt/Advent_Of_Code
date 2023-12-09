import itertools
from pathlib import Path

PUZZLE_FILENAME = "Day_9/puzzle_input.txt"


def get_puzzle_lines() -> list[str]:
    with Path(PUZZLE_FILENAME).open("r") as f:
        return f.readlines()


def main() -> None:
    lines = get_puzzle_lines()
    diff_per_step: list[list[list[int]]] = []
    for line in lines:
        step = []
        step.append(list(map(int, line.split())))
        diff = [int(y) - int(x) for x, y in itertools.pairwise(line.split())]
        step.append(diff)
        while not all(v == 0 for v in diff):
            diff = [int(y) - int(x) for x, y in itertools.pairwise(diff)]
            step.append(diff)
        diff_per_step.append(step)

    for v in diff_per_step:
        previous_elem = 0
        for elem in reversed(v):
            elem.append(previous_elem + elem[-1])
            previous_elem = elem[-1]
    print(diff_per_step)

    print(sum([x[0][-1] for x in diff_per_step]))


if __name__ == "__main__":
    main()
