import math
import re
from pathlib import Path

PUZZLE_FILENAME = "Day_8/puzzle_input.txt"


def get_puzzle_lines() -> str:
    with Path(PUZZLE_FILENAME).open("r") as f:
        return f.read()


def main() -> None:
    instruct, _, *networks = get_puzzle_lines().split("\n")
    my_table = str.maketrans("LR", "01")
    instructs = instruct.translate(my_table)
    letters = [re.findall(r"\w{3}", network) for network in networks]
    network_dict = {x[0]: (x[1], x[2]) for x in letters}

    starting_points = filter(lambda x: x.endswith("A"), network_dict.keys())
    nodes = list(starting_points)

    meeting_z = []
    for node in nodes:
        counter = 0
        while not node.endswith("Z"):
            for instruct in instructs:
                node = network_dict[node][int(instruct)]
                counter += 1
        meeting_z.append(counter)
        print(meeting_z)

    print(math.lcm(*meeting_z))


if __name__ == "__main__":
    main()
