from pathlib import Path

PUZZLE_FILENAME = "Day_12_Hot_Springs/example.txt"


def get_puzzle_lines() -> list[str]:
    with Path(PUZZLE_FILENAME).open("r") as f:
        return f.read().splitlines()


def main() -> None:
    grid = get_puzzle_lines()


if __name__ == "__main__":
    main()
