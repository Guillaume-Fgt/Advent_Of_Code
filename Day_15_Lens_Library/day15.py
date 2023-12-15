import re

with open("Day_15_Lens_Library/puzzle_input.txt") as f:
    seq = f.read().split(",")

result = 0
boxes: dict[int, list[str]] = {x: [] for x in range(256)}

for step in seq:
    pattern = re.compile(r"(\w+)([=-])(\d*)")
    _, letter, op, num, _ = re.split(pattern, step)

    label = 0
    for char in letter:
        label += ord(char)
        label *= 17
        label = label % 256
    if op == "-" and f"{letter} {num}" in boxes[label]:
        boxes[label].remove(f"{letter} {num}")
    if op == "-" and not num:
        for v in boxes[label]:
            if v.startswith(letter):
                boxes[label].remove(v)
    if op == "=":
        for i, v in enumerate(boxes[label]):
            if v.startswith(letter):
                boxes[label][i] = f"{letter} {num}"
                break
        else:
            boxes[label].append(f"{letter} {num}")

focus_power = 0
for key, values in boxes.items():
    for value in values:
        focus_power += (key + 1) * (values.index(value) + 1) * int(value.split()[-1])

print(focus_power)
