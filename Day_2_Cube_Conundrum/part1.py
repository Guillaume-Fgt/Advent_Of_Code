import re

PUZZLE_FILENAME = "Day_2_Cube_Conundrum/puzzle_input.txt"
MAX = {"red": 12, "green": 13, "blue": 14}


def get_puzzle_lines() -> list[str]:
    with open(PUZZLE_FILENAME) as f:
        return f.readlines()


def main():
    lines = get_puzzle_lines()
    game_total = 0
    for line in lines:
        game_num = line.split(":")[0].split()[1]
        color_valid = []
        for color in ("red", "green", "blue"):
            color_re = re.compile(rf"(\d+) {color}")
            color_values = re.findall(color_re, line)
            color_valid.append(all(int(x) <= MAX[color] for x in color_values))
        if all(color_valid):
            game_total += int(game_num)
            print(game_total)


if __name__ == "__main__":
    main()
