from pathlib import Path

PUZZLE_FILENAME = "Day_11_Cosmic_Expansion/puzzle_input.txt"


def get_puzzle_lines() -> list[str]:
    with Path(PUZZLE_FILENAME).open("r") as f:
        return f.read().splitlines()


def main() -> None:
    grid = get_puzzle_lines()
    empty_rows = [r for r, row in enumerate(grid) if all(char == "." for char in row)]
    empty_cols = [
        c for c, col in enumerate(zip(*grid)) if all(char == "." for char in col)
    ]
    points = [
        (r, c) for r, row in enumerate(grid) for c, ch in enumerate(row) if ch == "#"
    ]

    total = 0
    scale = 1_000_000
    for i, (r1, c1) in enumerate(points):
        for r2, c2 in points[:i]:
            for r in range(min(r1, r2), max(r1, r2)):
                total += scale if r in empty_rows else 1
            for c in range(min(c1, c2), max(c1, c2)):
                total += scale if c in empty_cols else 1

    print(total)


if __name__ == "__main__":
    main()
