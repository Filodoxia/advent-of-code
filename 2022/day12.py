from enum import Enum
from pathlib import Path
import math

import input


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


def dijkstra(hm: list[list[str]], start: complex, target: complex):
    m = len(hm)
    n = len(hm[0])

    # initialize
    visited: list[list[tuple[complex | None, float]]] = [
        [(None, math.inf)]*n for _ in range(m)
    ]
    visited[int(start.real)][int(start.imag)] = (None, 0)
    candidates: list[complex] = [start]
    # for a in range(m):
    #     for b in range(n):
    #         candidates.append(a + b*1j)
    # candidates.sort(
    #     key=lambda x: visited[int(x.real)][int(x.imag)][1],
    #     reverse=True
    # )

    while candidates:
        currentPos = candidates.pop()
        curPosX = int(currentPos.real)
        curPosY = int(currentPos.imag)
        currentHeight = ord(hm[curPosX][curPosY])

        # update neighbors
        neighbors: list[complex] = []

        if currentPos.real > 0:
            nn = currentPos + Direction.NORTH.value
            if currentHeight - ord(hm[int(nn.real)][int(nn.imag)]) >= -1:
                neighbors.append(nn)
        if currentPos.imag < n-1:
            ne = currentPos + Direction.EAST.value
            if currentHeight - ord(hm[int(ne.real)][int(ne.imag)]) >= -1:
                neighbors.append(ne)
        if currentPos.real < m-1:
            ns = currentPos + Direction.SOUTH.value
            if currentHeight - ord(hm[int(ns.real)][int(ns.imag)]) >= -1:
                neighbors.append(ns)
        if currentPos.imag > 0:
            nw = currentPos + Direction.WEST.value
            if currentHeight - ord(hm[int(nw.real)][int(nw.imag)]) >= -1:
                neighbors.append(nw)

        # print(f"""{currentPos} => {neighbors}""")
        curPosDist = visited[curPosX][curPosY][1]
        for nb in neighbors:
            nbX = int(nb.real)
            nbY = int(nb.imag)

            # print(curPosX, curPosY, nbX, nbY)
            # print(visited[curPosX][curPosY], visited[nbX][nbY])

            # if the position has never been visited add it to the candidates
            if visited[nbX][nbY][1] == math.inf:
                candidates.append(nb)

            # update distance to and predecessor of neighbor
            if curPosDist+1 < visited[nbX][nbY][1]:
                visited[nbX][nbY] = (currentPos, curPosDist+1)

        # keep candidates sorted
        candidates.sort(
            key=lambda x: visited[int(x.real)][int(x.imag)][1],
            reverse=True
        )

    return visited


def getShortestPath(visited: list[list[tuple[complex | None, float]]], finishPos: complex):
    next = finishPos
    path: list[complex] = []

    while next is not None:
        path.append(next)
        next = visited[int(next.real)][int(next.imag)][0]

    path.reverse()
    return path


def writeResult(hm: list[list[str]], path: list[complex], filename: str):
    s = "█"
    # replace
    for p in path:
        hm[int(p.real)][int(p.imag)] = s

    hm[int(path[0].real)][int(path[0].imag)] = "S"
    hm[int(path[-1].real)][int(path[-1].imag)] = "E"

    outPath = Path("./output")
    outPath.mkdir(exist_ok=True)

    with open(outPath.joinpath(filename), "w", encoding="utf8") as f:
        f.writelines(["".join(x) + "\n" for x in hm])


def star1():
    # height map
    hm = getInput()
    startPos, finishPos = findStartFinish(hm)
    hm[int(startPos.real)][int(startPos.imag)] = 'a'
    hm[int(finishPos.real)][int(finishPos.imag)] = 'z'

    r = dijkstra(hm, startPos, finishPos)
    sp = getShortestPath(r, finishPos)

    # print(",".join(map(str, sp)))
    writeResult(hm, sp, f"day{DAY}_1.txt")

    return f"Shortest distance is {r[int(finishPos.real)][int(finishPos.imag)][1]} from ({int(startPos.real)}, {int(startPos.imag)})"


def star2():
    # height map
    hm = getInput()
    startPos, finishPos = findStartFinish(hm)
    hm[int(startPos.real)][int(startPos.imag)] = 'a'
    hm[int(finishPos.real)][int(finishPos.imag)] = 'z'

    shortestDistance = math.inf
    bestStartPosition = None

    for x in range(len(hm)):
        for y in range(len(hm[0])):
            if hm[x][y] != "a":
                continue
            candidatePosition = x + y*1j
            d = dijkstra(hm, candidatePosition, finishPos)
            if d[int(finishPos.real)][int(finishPos.imag)][1] < shortestDistance:
                dBest = d
                bestStartPosition = candidatePosition
                shortestDistance = d[int(finishPos.real)
                                     ][int(finishPos.imag)][1]

    sp = getShortestPath(dBest, finishPos)

    # print(",".join(map(str, sp)))
    writeResult(hm, sp, f"day{DAY}_2.txt")

    return f"Shortest distance is {shortestDistance} from ({int(bestStartPosition.real)}, {int(bestStartPosition.imag)})"


if __name__ == "__main__":
    print(star1())
    print(star2())
