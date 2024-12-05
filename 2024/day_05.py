from collections import defaultdict

import aoc_lube

RAW = aoc_lube.fetch(year=2024, day=5)

def parse_raw():
    rules, updates = RAW.split("\n\n")
    rules_dict = defaultdict(set)
    for rule in rules.splitlines():
        page_num1, page_num2 = rule.split("|")
        rules_dict[int(page_num1)].add(int(page_num2))
    return rules_dict, updates


def part_one():
    rules_dict, updates = parse_raw()
    valid_updates = []
    for update_line in updates.splitlines():
        update = [int(x) for x in update_line.split(",")]
        valid = True
        for i, value in enumerate(update):
            if not rules_dict[value].isdisjoint(set(update[0:i])):
                valid = False
                break
        if valid:
            valid_updates.append(update)

    total = 0
    for updates in valid_updates:
        total += updates[len(updates) // 2]
    return total

def part_two():
    rules_dict, updates = parse_raw()
    valid_updates = []
    for update_line in updates.splitlines():
        update = [int(x) for x in update_line.split(",")]
        valid = False
        corrected = False
        while not valid:
            for i, value in enumerate(update):
                if rules_dict[value].isdisjoint(set(update[0:i])):
                    valid = True
                else:
                    valid = False
                    corrected = True
                    update.insert(i - 1, update.pop(i))
                    break
        if corrected:
            valid_updates.append(update)

    total = 0
    for updates in valid_updates:
        total += updates[len(updates) // 2]
    return total


aoc_lube.submit(year=2024, day=5, part=1, solution=part_one)
aoc_lube.submit(year=2024, day=5, part=2, solution=part_two)
