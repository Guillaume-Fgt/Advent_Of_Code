PUZZLE_FILENAME = "Day_1_Trebuchet/puzzle_input.txt"
TO_DIGIT = {
    "one": "o1ne",
    "two": "t2wo",
    "three": "th3ree",
    "four": "f4our",
    "five": "f5ive",
    "six": "s6ix",
    "seven": "s7ven",
    "eight": "ei8ght",
    "nine": "n9ine",
    "1": "1",
    "2": "2",
    "3": "3",
    "4": "4",
    "5": "5",
    "6": "6",
    "7": "7",
    "8": "8",
    "9": "9",
}


def get_puzzle_lines() -> list[str]:
    with open(PUZZLE_FILENAME) as f:
        return f.readlines()


def translate(line: str) -> str:
    for element in TO_DIGIT:
        new = line.replace(element, TO_DIGIT[element])
        line = new
    return line


def get_first_and_last(digit: str) -> int:
    return int(digit[0] + digit[-1])


def filter_digit(line: str) -> str:
    return "".join(filter(str.isdigit, line))


def main() -> None:
    lines = get_puzzle_lines()
    translation = [translate(line) for line in lines]
    digits = map(filter_digit, translation)
    first_last = [get_first_and_last(digit) for digit in digits]
    print(sum(first_last))


if __name__ == "__main__":
    main()
