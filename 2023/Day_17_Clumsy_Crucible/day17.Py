from heapq import heappop, heappush

with open("Day_17_Clumsy_Crucible/puzzle_input.txt") as f:
    grid = f.read().rstrip()


def int_grid(raw, np=True, separator=""):
    """Parse a grid of ints into a 2d list or numpy array (if np==True)."""
    array = [
        [int(i) for i in (line.split(separator) if separator else line) if i]
        for line in raw.splitlines()
    ]

    if np:
        import numpy as np

        return np.array(array)

    return array


grid = int_grid(grid)
H, W = grid.shape


def min_heatloss(mn, mx):
    heap = [(0, 0, 0, 1, 0), (0, 0, 0, 0, 1)]
    heatlosses = {}
    while heap:
        heatloss, y, x, Δy, Δx = heappop(heap)
        if y == H - 1 and x == W - 1:
            return heatloss

        for Δy, Δx in ((-Δx, Δy), (Δx, -Δy)):
            Δheatloss = 0
            for d in range(1, mx + 1):
                v = y + Δy * d
                u = x + Δx * d

                if not (0 <= v < H and 0 <= u < W):
                    break

                Δheatloss += grid[v, u]

                if d >= mn:
                    new_heatloss = heatloss + Δheatloss
                    if heatlosses.get((v, u, Δy, Δx), float("inf")) > new_heatloss:
                        heatlosses[v, u, Δy, Δx] = new_heatloss
                        heappush(heap, (new_heatloss, v, u, Δy, Δx))
    return heatlosses


print(min_heatloss(1, 3))
print(min_heatloss(4, 10))
