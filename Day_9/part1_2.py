from pathlib import Path

PUZZLE_FILENAME = "Day_9/example.txt"


def get_puzzle_lines() -> str:
    with Path(PUZZLE_FILENAME).open("r") as f:
        return f.read()


def main() -> None:
    lines = get_puzzle_lines()


if __name__ == "__main__":
    main()
