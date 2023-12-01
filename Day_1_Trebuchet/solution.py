from collections import defaultdict

PUZZLE_FILENAME = "Day_1_Trebuchet/puzzle_input.txt"
TO_DIGIT = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
    "1": 1,
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
}


def findall(number: str, line: str) -> list[tuple[int, int]]:
    result = []
    i = line.find(number)
    while i != -1:
        result.append((TO_DIGIT[number], i))
        i = line.find(number, i + 1)
    return result


def get_puzzle_lines() -> list[str]:
    with open(PUZZLE_FILENAME) as f:
        return f.readlines()


def pos_nums(line: str) -> defaultdict[str, list[str, int]]:
    result = defaultdict(list)
    for number in TO_DIGIT:
        find_all = findall(number, line)
        if find_all:
            for x in find_all:
                result["pos"].append(x)
    for element in result.values():
        element.sort(key=lambda x: x[1])
    return result


def main() -> None:
    lines = get_puzzle_lines()
    pos_nums_list = [pos_nums(line) for line in lines]
    total = 0
    for element in pos_nums_list:
        for x in element.values():
            total += int(str(x[0][0]) + str(x[-1][0]))
    print(total)


if __name__ == "__main__":
    main()
