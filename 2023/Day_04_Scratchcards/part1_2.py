from pathlib import Path

PUZZLE_FILENAME = "Day_4_Scratchcards/puzzle_input.txt"


def get_puzzle_lines() -> list[str]:
    with Path(PUZZLE_FILENAME).open("r") as f:
        return f.readlines()


def main() -> None:
    lines = get_puzzle_lines()
    s = 0
    cards = [1 for _ in lines]

    for index, line in enumerate(lines):
        a, b = line.split(":")[1].split("|")
        n = len(set(a.split()) & set(b.split()))

        if n > 0:
            s += 2 ** (n - 1)

        for i in range(n):
            cards[index + i + 1] += cards[index]

    print(s, sum(cards))


if __name__ == "__main__":
    main()
