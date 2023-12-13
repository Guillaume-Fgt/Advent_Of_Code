from functools import cache
from pathlib import Path

PUZZLE_FILENAME = "Day_12_Hot_Springs/puzzle_input.txt"


def get_puzzle_lines() -> list[str]:
    with Path(PUZZLE_FILENAME).open("r") as f:
        return f.read().splitlines()


@cache
def count(cfg: str, nums: tuple[int]) -> int:
    if cfg == "":
        return 1 if nums == () else 0
    if nums == ():
        return 0 if "#" in cfg else 1

    result = 0
    if cfg[0] in ".?":
        result += count(cfg[1:], nums)
    if cfg[0] in "#?":
        if (
            nums[0] <= len(cfg)
            and "." not in cfg[: nums[0]]
            and (nums[0] == len(cfg) or cfg[nums[0]] != "#")
        ):
            result += count(cfg[nums[0] + 1 :], nums[1:])
        else:
            result += 0
    return result


def main() -> None:
    grid = get_puzzle_lines()
    total = 0
    for line in grid:
        cfg, nums = line.split()
        nums = tuple(map(int, nums.split(",")))
        cfg = "?".join([cfg] * 5)
        nums *= 5
        total += count(cfg, nums)
    print(total)


if __name__ == "__main__":
    main()
