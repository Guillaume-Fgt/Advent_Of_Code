PUZZLE_FILENAME = "Day_1_Trebuchet/puzzle_input.txt"


def get_puzzle_lines() -> list[str]:
    with open(PUZZLE_FILENAME) as f:
        return f.readlines()


def filter_digit(line: str) -> str:
    return "".join(filter(str.isdigit, line))


def main():
    lines = get_puzzle_lines()
    digits = map(filter_digit, lines)
    print(list(digits))


if __name__ == "__main__":
    main()
