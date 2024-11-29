with open("Day_16_The_Floor_Will_Be_Lava/puzzle_input.txt") as f:
    grid = f.read().splitlines()

H, W = len(grid), len(grid[0])


def bounce(start):
    states = set()
    positions = set()
    stack = [start]

    while stack:
        y, x, dy, dx = stack.pop()
        if (y, x, dy, dx) in states:
            continue
        states.add((y, x, dy, dx))

        y += dy
        x += dx

        if not (0 <= y < H and 0 <= x < W):
            continue

        match grid[y][x]:
            case "/":
                dy, dx = -dx, -dy
            case "\\":
                dy, dx = dx, dy
            case "|" if dx:
                stack.append((y, x, -1, 0))
                dy, dx = 1, 0
            case "-" if dy:
                stack.append((y, x, 0, -1))
                dy, dx = 0, 1

        positions.add((y, x))
        stack.append((y, x, dy, dx))

    return len(positions)


print(bounce((0, -1, 0, 1)))


def grid_boundary_points():
    for y in range(H):
        yield y, -1, 0, 1
        yield y, W, 0, -1
    for x in range(W):
        yield -1, x, 1, 0
        yield H, x, -1, 0


print(max(map(bounce, grid_boundary_points())))
