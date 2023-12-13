from pathlib import Path

PUZZLE_FILENAME = "Day_13/puzzle_input.txt"


def get_puzzle_lines() -> list[str]:
    with Path(PUZZLE_FILENAME).open("r") as f:
        return f.read().split("\n\n")


def find_mirror(grid: list[str]) -> int:
    for r in range(1, len(grid)):
        above = grid[:r][::-1]
        below = grid[r:]

        if (
            sum(
                sum(0 if a == b else 1 for a, b in zip(x, y))
                for x, y in zip(above, below)
            )
            == 1
        ):
            return r
    return 0


def main() -> None:
    total = 0

    for block in get_puzzle_lines():
        grid = block.splitlines()

        row = find_mirror(grid)
        total += row * 100

        col = find_mirror(list(zip(*grid)))
        total += col

    print(total)


if __name__ == "__main__":
    main()
