from collections import Counter
from pathlib import Path

PUZZLE_FILENAME = "Day_7/puzzle_input.txt"


def get_puzzle_lines() -> list[str]:
    with Path(PUZZLE_FILENAME).open("r") as f:
        return f.readlines()


CARDS = ("J", "2", "3", "4", "5", "6", "7", "8", "9", "T", "Q", "K", "A")
HAND_TYPE = {
    (1, 1, 1, 1, 1): ("High card", 0),
    (2, 1, 1, 1): ("One pair", 1),
    (2, 2, 1): ("Two pair", 2),
    (3, 1, 1): ("Three of a kind", 3),
    (3, 2): ("Full house", 4),
    (4, 1): ("Four of a kind", 5),
    (5,): ("Five of a kind", 6),
}


def get_hand_type(hand: str) -> str:
    count = Counter(hand)
    if "J" in hand:
        if hand.count("J") == 5:
            return HAND_TYPE[(5,)]
        key_to_up = (
            count.most_common(1)[0][0]
            if count.most_common(1)[0][0] != "J"
            else count.most_common(2)[1][0]
        )
        d = Counter(
            {"J": -count["J"], key_to_up: count["J"]},
        )
        count.update(d)
        del count["J"]
    return HAND_TYPE[tuple(x[1] for x in count.most_common())]


def order_hands(hand: list[str]) -> tuple[str, list[int]]:
    return (hand[2][1], [CARDS.index(card) for card in hand[0]])


def main() -> None:
    lines = get_puzzle_lines()
    hands = [line.split() for line in lines]
    for hand in hands:
        hand.append(get_hand_type(hand[0]))
    # hands.sort(key=lambda x: x[2][1])
    hands.sort(key=lambda x: order_hands(x))

    print(sum([int(x[1]) * (hands.index(x) + 1) for x in hands]))


if __name__ == "__main__":
    main()
