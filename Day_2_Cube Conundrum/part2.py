import functools
import re

PUZZLE_FILENAME = "Day_2_Cube Conundrum/puzzle_input.txt"
MAX = {"red": 12, "green": 13, "blue": 14}


def get_puzzle_lines() -> list[str]:
    with open(PUZZLE_FILENAME) as f:
        return f.readlines()


def main() -> None:
    lines = get_puzzle_lines()
    game_total = 0
    for line in lines:
        color_max = []
        for color in ("red", "green", "blue"):
            color_re = re.compile(rf"(\d+) {color}")
            color_values = re.findall(color_re, line)
            color_max.append(max([int(value) for value in color_values]))
        game_total += functools.reduce(lambda x, y: x * y, color_max)
    print(game_total)


if __name__ == "__main__":
    main()
