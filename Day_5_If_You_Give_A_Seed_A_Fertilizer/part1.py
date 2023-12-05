from pathlib import Path

PUZZLE_FILENAME = "Day_5_If_You_Give_A_Seed_A_Fertilizer/puzzle_input.txt"


def get_puzzle_lines() -> str:
    with Path(PUZZLE_FILENAME).open("r") as f:
        return f.read()


def main() -> None:
    data = get_puzzle_lines()
    seeds_value, *maps = data.split("\n\n")
    seeds = {int(x) for x in seeds_value.split(":")[1].split()}
    dict_conv = {}
    for alma_map in maps:
        title, *values = alma_map.split("\n")
        dict_conv[title] = {}
        for value in values:
            dest, source, ran_len = value.split()
            for x, y in zip(
                range(int(source), int(source) + int(ran_len)),
                range(int(dest), int(dest) + int(ran_len)),
            ):
                dict_conv[title][x] = y
    print(dict_conv)

    # searched_result = []
    # for seed in seeds:
    #     searched = seed
    #     for key, value in dict_conv.items():
    #         if value.get(searched):
    #             print(f"{key}, old value: {searched }, new value: {value[searched ]}")
    #             searched = value[searched]
    #         else:
    #             print(f"{key}, value stay the same: {searched }")
    #     searched_result.append(searched)
    # print(searched_result)


if __name__ == "__main__":
    main()
