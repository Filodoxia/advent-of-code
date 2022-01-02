from typing import List, Set, Tuple
import input as inp
import re


def star1():
    dots, instructions = parseInput()

    for foldingDimension, linePosition in instructions[:1]:
        if foldingDimension == "x":
            dots = fold(dots, x=linePosition)
        else:
            dots = fold(dots, y=linePosition)

    print(len(dots))


def star2():
    dots, instructions = parseInput()

    for foldingDimension, linePosition in instructions:
        if foldingDimension == "x":
            dots = fold(dots, x=linePosition)
        else:
            dots = fold(dots, y=linePosition)

    maxX = 0
    maxY = 0

    for dot in dots:
        maxX = max(maxX, dot[0])
        maxY = max(maxY, dot[1])

    raster = [[" " for _ in range(maxX+1)] for _ in range(maxY+1)]

    for dot in dots:
        raster[dot[1]][dot[0]] = chr(9608)

    for row in raster:
        print("".join(row))


def fold(dots: Set[Tuple[int, int]], x: int = None, y: int = None) -> Set[Tuple[int, int]]:
    if not bool(x) ^ bool(y):
        raise Exception("Must specify x or y but not both")

    print(len(dots), x, y)
    newDots = set()
    for dot in dots:
        if x:
            if dot[0] == x:
                raise Exception("No dots on folding line allowed")
            if dot[0] > x:
                newDot = ((x-1) - (dot[0] % (x+1)), dot[1])
                newDots.add(newDot)
                # print(f"{dot} -> {newDot}")
            else:
                newDots.add((dot[0], dot[1]))
        else:
            if dot[1] == y:
                raise Exception("No dots on folding line allowed")
            if dot[1] > y:
                newDot = (dot[0], (y-1) - (dot[1] % (y+1)))
                newDots.add(newDot)
                # print(f"{dot} -> {newDot}")
            else:
                newDots.add((dot[0], dot[1]))
    return newDots


def parseInput():
    dots = set()
    instructions = []

    regex = re.compile("^fold along (x|y)=(\d+)$")

    for line in inp.read(13):
        if line[0] == "f":
            matches = regex.match(line)
            instructions.append((matches.group(1), int(matches.group(2))))
        elif not line[0] == "\n":
            dots.add(tuple(map(int, line.strip().split(","))))

    return dots, instructions


if __name__ == "__main__":
    star1()
    star2()
