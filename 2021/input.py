from os import path


def read(day: int):
    return open(path.join(path.dirname(__file__), "input", f"day{day}"), "r")


def readIntArray(day: int):
    filePath = path.join(path.dirname(__file__), "input", f"day{day}")
    with open(filePath, "r") as input:
        a = list(map(int, input.readline().split(",")))
    return a


def readIntArray2d(day: int, separator: str = ","):
    filePath = path.join(path.dirname(__file__), "input", f"day{day}")
    a = []
    with open(filePath, "r") as input:
        for line in input:
            if separator:
                a.append(list(map(int, line.split(","))))
            else:
                a.append(list(map(int, list(line.strip()))))
    return a
