import input
from enum import Enum
import math
import sys


MAX_STEPS = 1_000_000_000
STEPS = 0
DAY = 12
TEST = False
DEBUG = False


class Direction(Enum):
    NORTH = -1+0j
    EAST = 0+1j
    SOUTH = 1+0j
    WEST = 0-1j


def getInput():
    return input.readGrid(f"day{DAY}{'_test' if TEST else ''}.txt", inLineSep=None, asInt=False)


def findStartFinish(hm: list[list[str]]):
    foundStart = False
    foundFinish = False

    for x in range(len(hm)):
        for y in range(len(hm[x])):
            if hm[x][y] == "S":
                startPos = x + y*1j
                foundStart = True
                if foundFinish:
                    return (startPos, finishPos)
            elif hm[x][y] == "E":
                finishPos = x + y*1j
                foundFinish = True
                if foundStart:
                    return (startPos, finishPos)

    raise Exception("No start tile found")


def star1():
    # height map
    hm = getInput()
    # n = len(hm)
    # m = len(hm[0])

    # visited = [[False]*m]*n
    # v = 0
    # print(visited)
    startPos, finishPos = findStartFinish(hm)
    hm[int(startPos.real)][int(startPos.imag)] = 'a'
    hm[int(finishPos.real)][int(finishPos.imag)] = 'z'
    path, steps = flood([startPos], hm, math.inf, finishPos)

    return f"\n\n==========================================================\nStar 1: {steps-1}\n{path}"


def flood(path: list[complex], hm, upperBound: float, finishPos: complex) -> tuple[list[complex], float]:
    global STEPS
    STEPS += 1
    if STEPS % 100_000 == 0:
        print(STEPS, len(path), path[-1], upperBound)
    if STEPS > MAX_STEPS:
        sys.exit(1)

    viableDirections: list[tuple[Direction, int]] = []
    cpX = int(path[-1].real)  # current position X
    cpY = int(path[-1].imag)  # current position Y
    currentHeight = ord(hm[cpX][cpY])

    if DEBUG:
        print(
            f"""\nCurrent Position: ({cpX},{cpY}); Height: {currentHeight}""")

    # no need to check further, better solution already found
    if len(path) >= upperBound:
        return (path, upperBound)

    # finish position found and it's the best solution, because check for better solution failed
    if path[-1] == finishPos:
        print("Found Finish")
        return (path, len(path))

    if cpX > 0:
        if currentHeight - ord(hm[cpX-1][cpY]) >= -1:
            # no moving back or running in circles
            # if (cpX-1, cpY) not in path:
            viableDirections.append(
                (Direction.NORTH, currentHeight - ord(hm[cpX-1][cpY])))

    if cpY < len(hm[cpX])-1:
        if currentHeight - ord(hm[cpX][cpY+1]) >= -1:
            # no moving back or running in circles
            # if (cpX, cpY+1) not in path:
            viableDirections.append(
                (Direction.EAST, currentHeight - ord(hm[cpX][cpY+1])))

    if cpX < len(hm)-1:
        if currentHeight - ord(hm[cpX+1][cpY]) >= -1:
            # no moving back or running in circles
            # if (cpX+1, cpY) not in path:
            viableDirections.append(
                (Direction.SOUTH, currentHeight - ord(hm[cpX+1][cpY])))

    if cpY > 0:
        if currentHeight - ord(hm[cpX][cpY-1]) >= -1:
            # no moving back or running in circles
            # if (cpX, cpY-1) not in path:
            viableDirections.append(
                (Direction.WEST, currentHeight - ord(hm[cpX][cpY-1])))

    if DEBUG:
        print(f"""Viable: {[d[0].name for d in viableDirections]}""")

    paths: list[tuple[list[complex], float]] = []
    for d in sorted(viableDirections, key=lambda x: x[1]):
        # no moving back or running in circles
        nextPos = path[-1]+d[0].value
        if nextPos not in path:
            newPath = path.copy()
            newPath.append(nextPos)

            if DEBUG:
                print(f"""Move {d[0].name} to {nextPos}""")

            paths.append(flood(newPath, hm, upperBound, finishPos))

    if DEBUG:
        print(f"""({cpX},{cpY}) candidates: {paths}""")

    if paths:
        best = sorted(paths, key=lambda x: x[1])[0]
        if best[1] < upperBound:
            return best

    return path, upperBound


def star2():
    hm = getInput()

    return "Star 2:"


if __name__ == "__main__":
    print(star1())
    print(star2())
