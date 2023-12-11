import itertools
from pathlib import Path

PUZZLE_FILENAME = "Day_10_Pipe_Maze/puzzle_input.txt"


def get_puzzle_lines() -> list[str]:
    with Path(PUZZLE_FILENAME).open("r") as f:
        return f.read().splitlines()


def is_in_boundaries(line: int, column: int, maze: list[str]) -> bool:
    return 0 <= line < len(maze) and 0 <= column < len(maze[0])


def voisins(pos: tuple[int, int], maze: list[str]):
    i, j = pos
    n, m = len(maze), len(maze[0])
    c = maze[i][j]
    match c:
        case "|":
            voisinspot = [(i + 1, j), (i - 1, j)]
        case "-":
            voisinspot = [(i, j - 1), (i, j + 1)]
        case "L":
            voisinspot = [(i - 1, j), (i, j + 1)]
        case "J" | "S":
            voisinspot = [(i - 1, j), (i, j - 1)]
        case "7":
            voisinspot = [(i + 1, j), (i, j - 1)]
        case "F":
            voisinspot = [(i + 1, j), (i, j + 1)]
    return [(i, j) for (i, j) in voisinspot if is_in_boundaries(i, j, maze)]


def main() -> None:
    maze = get_puzzle_lines()
    n, m = len(maze), len(maze[0])
    start = None
    for i, j in itertools.product(range(n), range(m)):
        if maze[i][j] == "S":
            start = (i, j)
            break
    if not start:
        msg = "Start not found"
        raise ValueError(msg)

    # BFS
    file = [start]
    dist = {start: 0}
    while len(file) > 0:
        new = file.pop(0)
        for s in voisins(new, maze):
            if s not in dist:
                file.append(s)
                dist[s] = dist[new] + 1

    print("Part 1 :", max([d for v, d in dist.items()]))

    inside = 0
    for i in range(n):
        for j in range(m):
            if (i, j) not in dist:
                counter = len(
                    [
                        (i, l)
                        for l in range(j)
                        if (i, l) in dist and maze[i][l] not in {"-", "J", "L", "S"}
                    ],
                )  # if your S is a -, J or L put it here too
                inside += counter % 2

    print("Part 2 :", inside)


if __name__ == "__main__":
    main()
