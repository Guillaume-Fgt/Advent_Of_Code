import itertools
from pathlib import Path

PUZZLE_FILENAME = "Day_5_If_You_Give_A_Seed_A_Fertilizer/puzzle_input.txt"


def get_puzzle_lines() -> str:
    with Path(PUZZLE_FILENAME).open("r") as f:
        return f.read()


def main() -> None:
    inputs, *to_maps = get_puzzle_lines().split("\n\n")
    inputs = list(map(int, inputs.split(":")[1].split()))
    seeds = [(x, x + y) for x, y in itertools.batched(inputs, 2)]

    for elem in to_maps:
        maps = [list(map(int, line.split())) for line in elem.splitlines()[1:]]
        new = []
        while len(seeds) > 0:
            s, e = seeds.pop()
            for a, b, c in maps:
                os = max(s, b)
                oe = min(e, b + c)
                if not os < oe:
                    continue
                new.append((os - b + a, oe - b + a))
                if os > s:
                    seeds.append((s, os))
                if e > oe:
                    seeds.append((oe, e))
                break
            else:
                new.append((s, e))
        seeds = new

    print(min(seeds)[0])


if __name__ == "__main__":
    main()
