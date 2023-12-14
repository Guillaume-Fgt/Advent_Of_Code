with open("Day_14_Parabolic_Reflector_Dish/puzzle_input.txt") as f:
    grid = tuple(f.read().splitlines())


def cycle():
    global grid
    for _ in range(4):
        grid = tuple(map("".join, zip(*grid)))
        grid = tuple(
            "#".join("".join(sorted(group, reverse=True)) for group in row.split("#"))
            for row in grid
        )
        grid = tuple(row[::-1] for row in grid)


seen = {grid}
array = [grid]

iteration = 0
while True:
    iteration += 1
    cycle()
    if grid in seen:
        break
    seen.add(grid)
    array.append(grid)

first = array.index(grid)
grid = array[(1000000000 - first) % (iteration - first) + first]

print(sum(row.count("O") * (len(grid) - r) for r, row in enumerate(grid)))
