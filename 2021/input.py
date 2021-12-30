from os import path
from typing import List


def read(day: int):
    return open(path.join(path.dirname(__file__), "input", f"day{day}"), "r")


def readIntArray(day: int):
    filePath = path.join(path.dirname(__file__), "input", f"day{day}")
    with open(filePath, "r") as input:
        a = list(map(int, input.readline().split(",")))
    return a


def readIntArray2d(day: int, separator: str = None) -> List[List[int]]:
    filePath = path.join(path.dirname(__file__), "input", f"day{day}")
    a = []
    with open(filePath, "r") as input:
        for line in input:
            if separator:
                lineList = line.strip().split(",")
            else:
                lineList = list(line.strip())

            a.append(list(map(int, lineList)))
    return a
