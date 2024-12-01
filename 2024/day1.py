from pathlib import Path
from typing import Dict, List

DAY = 1

IN_PATH = Path(__file__).parent.joinpath(f"in/day{DAY}").resolve()
INPUT = open(IN_PATH, mode="r").readlines()


def star1():
    list_left = []
    list_right = []

    for line in INPUT:
        items = line.split("   ")
        list_left.append(int(items[0]))
        list_right.append(int(items[1]))

    list_left.sort()
    list_right.sort()

    distance = 0
    for l, r in zip(list_left, list_right):
        distance += abs(l - r)

    print(f"Part 1: {distance}")


def star2():
    list_left = []
    list_right = []

    for line in INPUT:
        items = line.split("   ")
        list_left.append(int(items[0]))
        list_right.append(int(items[1]))

    list_left.sort()
    histogram_right = build_histogram(list_right)

    distance = 0
    for l in list_left:
        count_right = histogram_right.get(l, 0)
        distance += abs(l * count_right)

    print(f"Part 2: {distance}")


def build_histogram(list: List[int]) -> Dict[int, int]:
    histogram = {}

    for item in list:
        histogram[item] = histogram.setdefault(item, 0) + 1

    return histogram


if __name__ == "__main__":
    star1()
    star2()
