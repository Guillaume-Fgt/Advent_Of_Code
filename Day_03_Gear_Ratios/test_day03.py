from part1_2 import get_special_chars


def test_get_special_chars() -> None:
    lines = ["..23*..23*"]
    assert get_special_chars(lines) == {(0, 4), (0, 9)}
