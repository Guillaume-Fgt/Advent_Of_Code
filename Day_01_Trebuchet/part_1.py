PUZZLE_FILENAME = "Day_1_Trebuchet/puzzle_input.txt"


def get_puzzle_lines() -> list[str]:
    with open(PUZZLE_FILENAME) as f:
        return f.readlines()


def filter_digit(line: str) -> str:
    return "".join(filter(str.isdigit, line))


def get_first_and_last(digit: str) -> int:
    return int(digit[0] + digit[-1])


def main():
    lines = get_puzzle_lines()
    digits = map(filter_digit, lines)
    first_last = [get_first_and_last(digit) for digit in digits]
    print(sum(first_last))


if __name__ == "__main__":
    main()
