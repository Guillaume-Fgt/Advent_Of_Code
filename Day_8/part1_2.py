from pathlib import Path

PUZZLE_FILENAME = "Day_8/example.txt"


def get_puzzle_lines() -> list[str]:
    with Path(PUZZLE_FILENAME).open("r") as f:
        return f.readlines()


def main() -> None:
    lines = get_puzzle_lines()


if __name__ == "__main__":
    main()
