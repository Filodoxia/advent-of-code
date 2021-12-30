from typing import List, Tuple
import input as inp
import os
import time

neighborCache = {}
FLASH_THRESHOLD = 10


def star1():
    octopi = inp.readIntArray2d(11)
    maxRow = len(octopi) - 1
    maxCol = len(octopi[0]) - 1

    cache(maxRow, maxCol)

    totalFlashes = 0

    print("-- Day 0 ----------")
    prettyPrint(octopi)
    for i in range(100):
        totalFlashes += iterate(octopi)

        os.system("cls")
        print(f"\n-- Day {i+1} ----------")
        prettyPrint(octopi)
        time.sleep(0.05)

    print(totalFlashes)


def star2():
    octopi = inp.readIntArray2d(11)
    maxRow = len(octopi) - 1
    maxCol = len(octopi[0]) - 1
    octopiCount = len(octopi)*len(octopi[0])

    cache(maxRow, maxCol)

    print("-- Day 0 ----------")
    prettyPrint(octopi)

    i = 0
    flashCount = 0

    while not flashCount == octopiCount:
        flashCount = iterate(octopi)
        i += 1

        os.system("cls")
        print(f"\n-- Day {i} ----------")
        prettyPrint(octopi)


def iterate(octopi: List[List[int]]) -> int:
    flashCount = 0
    maxRow = len(octopi) - 1
    maxCol = len(octopi[0]) - 1

    # keep track of octopi that already flashed this iteration
    flashed = dict([(i, []) for i in range(maxRow + 1)])

    # increase each energy level by 1
    for r in range(maxRow + 1):
        octopi[r] = list(map(lambda x: x + 1, octopi[r]))

    flashQueue = []

    # add all octopi tp the flash queue that "naturally" flash this iteration
    for r in range(maxRow + 1):
        for c in range(maxCol + 1):
            if octopi[r][c] == FLASH_THRESHOLD:
                flashQueue.append((r, c))

    # flash octopi in queue and if a flash leads to adjacent octopi to reach the
    # energy level threshold add them to the queue
    while len(flashQueue) > 0:
        octopus = flashQueue.pop()
        flashCount += 1
        flashed[octopus[0]].append(octopus[1])

        # increase energy level of neighbors
        for neighbor in neighborCache[(octopus[0], octopus[1])]:
            # print((octopus[0], octopus[1]), neighbor)
            octopi[neighbor[0]][neighbor[1]] += 1

            if octopi[neighbor[0]][neighbor[1]] == FLASH_THRESHOLD:
                flashQueue.append((neighbor[0], neighbor[1]))

    # reset energy level of all octopi that flashed
    for r, colList in flashed.items():
        for c in colList:
            octopi[r][c] = 0

    return flashCount


def cache(maxRow: int, maxCol: int):
    global neighborCache
    neighborCache = {}

    for r in range(maxRow + 1):
        for c in range(maxCol + 1):
            neighborCache.update({
                (r, c): findNeighbors((r, c), maxRow, maxCol)
            })


def findNeighbors(pos: Tuple[int, int], maxRow: int, maxCol: int) -> List[Tuple[int, int]]:
    """ Finds valid neighbors, incl. diagonals. pos is (row, col) not (x, y) """
    validNeighbors = []

    canGoUp = not pos[0] == 0
    canGoDown = not pos[0] == maxRow
    canGoLeft = not pos[1] == 0
    canGoRight = not pos[1] == maxCol

    if canGoUp:
        validNeighbors.append((pos[0] - 1, pos[1]))
        if canGoLeft:
            validNeighbors.append((pos[0] - 1, pos[1] - 1))
        if canGoRight:
            validNeighbors.append((pos[0] - 1, pos[1] + 1))
    if canGoDown:
        validNeighbors.append((pos[0] + 1, pos[1]))
        if canGoLeft:
            validNeighbors.append((pos[0] + 1, pos[1] - 1))
        if canGoRight:
            validNeighbors.append((pos[0] + 1, pos[1] + 1))
    if canGoLeft:
        validNeighbors.append((pos[0], pos[1] - 1))
    if canGoRight:
        validNeighbors.append((pos[0], pos[1] + 1))

    return validNeighbors


def prettyPrint(octopi: List[List[int]]):
    for row in octopi:
        s = " ".join(list(map(lambda x: chr(9608) if x == 0 else " ", row)))
        # s = " ".join(list(map(str, row))).replace("0", chr(9608))
        print(s)


if __name__ == "__main__":
    star1()
    star2()
