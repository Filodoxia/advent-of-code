from typing import List, Tuple
import input as inp
import re


class Line():
    start: Tuple[int, int]
    end: Tuple[int, int]

    def __init__(self, start: Tuple[int, int], end: Tuple[int, int]) -> None:
        self.start = start
        self.end = end

    def __str__(self) -> str:
        return f"""{self.start} -> {self.end}"""


def star1():
    print(f"""Number of overlaps: {determineOverlap(True)}""")


def star2():
    print(f"""Number of overlaps: {determineOverlap(False)}""")


def determineOverlap(ignoreDiagonalLines: bool) -> int:
    lines, origin, topRight = processInput()

    width = topRight[0] - origin[0] + 1
    height = topRight[1] - origin[1] + 1
    coordSystem = [[0]*width for i in range(height)]
    for line in lines:
        # print("-"*20)
        # print(line)
        if line.start[0] == line.end[0]:
            x = line.start[0] - origin[0]

            if line.start[1] < line.end[1]:
                lineLength = line.end[1] - line.start[1]
                yStart = line.start[1] - origin[1]
            else:
                lineLength = line.start[1] - line.end[1]
                yStart = line.end[1] - origin[1]

            for yOffset in range(lineLength + 1):
                yIndex = yStart + yOffset
                coordSystem[yIndex][x] += 1
                # autopep8: off
                # print(f"""({x},{yIndex}) => ({x + origin[0]},{yIndex + origin[1]})""")
                # autopep8: on
        elif line.start[1] == line.end[1]:
            y = line.start[1] - origin[1]

            if line.start[0] < line.end[0]:
                lineLength = line.end[0] - line.start[0]
                xStart = line.start[0] - origin[0]
            else:
                lineLength = line.start[0] - line.end[0]
                xStart = line.end[0] - origin[0]

            for xOffset in range(lineLength + 1):
                xIndex = xStart + xOffset
                coordSystem[y][xIndex] += 1
                # autopep8: off
                # print(f"""({xIndex},{y}) => ({xIndex + origin[0]},{y + origin[1]})""")
                # autopep8: on
        elif not ignoreDiagonalLines:
            slopeX = line.end[0] - line.start[0]
            slopeY = line.end[1] - line.start[1]
            swToNe = slopeX > 0 and slopeY > 0
            neToSw = slopeX < 0 and slopeY < 0
            nwToSe = slopeX > 0 and slopeY < 0
            seToNw = slopeX < 0 and slopeY > 0

            if swToNe:
                firstIndexX = line.start[0] - origin[0]
                firstIndexY = line.start[1] - origin[1]
                stepY = 1
            elif neToSw:
                firstIndexX = line.end[0] - origin[0]
                firstIndexY = line.end[1] - origin[1]
                stepY = 1
            elif nwToSe:
                firstIndexX = line.start[0] - origin[0]
                firstIndexY = line.start[1] - origin[1]
                stepY = -1
            elif seToNw:
                firstIndexX = line.end[0] - origin[0]
                firstIndexY = line.end[1] - origin[1]
                stepY = -1

            lineLength = abs(line.end[0] - line.start[0])

            for offset in range(lineLength + 1):
                x = firstIndexX + offset
                y = firstIndexY + (offset * stepY)
                coordSystem[y][x] += 1

        # printCoord(coordSystem, height)

    numberOfOverlaps = 0

    for y in range(height):
        for x in range(width):
            if coordSystem[y][x] > 1:
                numberOfOverlaps += 1

    # print(f"""Origin: {origin}""")
    # print(f"""Top right: {topRight}""")

    return numberOfOverlaps


def printCoord(coord, height):
    for y in range(height-1, -1, -1):
        print(coord[y])


def processInput() -> Tuple[List[Line], Tuple[int, int], Tuple[int, int]]:
    regex = re.compile(r"^(\d+),(\d+) -> (\d+),(\d+)")
    lines = []
    origin = []
    topRight = []

    with inp.read(5) as input:
        coordinates = list(map(int, regex.findall(input.readline())[0]))
        origin = [
            min(coordinates[0], coordinates[2]),
            min(coordinates[1], coordinates[3])
        ]
        topRight = [
            max(coordinates[0], coordinates[2]),
            max(coordinates[1], coordinates[3])
        ]
        line = Line(
            (coordinates[0], coordinates[1]),
            (coordinates[2], coordinates[3])
        )
        lines.append(line)

        for line in input:
            coordinates = list(map(int, regex.findall(line)[0]))

            if coordinates[0] < origin[0]:
                origin[0] = coordinates[0]
            if coordinates[0] > topRight[0]:
                topRight[0] = coordinates[0]

            if coordinates[1] < origin[1]:
                origin[1] = coordinates[1]
            if coordinates[1] > topRight[1]:
                topRight[1] = coordinates[1]

            if coordinates[2] < origin[0]:
                origin[0] = coordinates[2]
            if coordinates[2] > topRight[0]:
                topRight[0] = coordinates[2]

            if coordinates[3] < origin[1]:
                origin[1] = coordinates[3]
            if coordinates[3] > topRight[1]:
                topRight[1] = coordinates[3]

            line = Line(
                (coordinates[0], coordinates[1]),
                (coordinates[2], coordinates[3])
            )
            lines.append(line)

    return lines, tuple(origin), tuple(topRight)


if __name__ == "__main__":
    star1()
    star2()
