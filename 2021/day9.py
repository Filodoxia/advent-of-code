from typing import List, Tuple
import input as inp


def star1():
    hm = inp.readIntArray2d(9, None)  # heightmap
    lows = findLows(hm)

    riskLevel = 0
    for (r, c) in lows:
        riskLevel += 1 + hm[r][c]
    print(f"Risk level: {riskLevel}")


def star2():
    hm = inp.readIntArray2d(9, None)  # heightmap
    lows = findLows(hm)
    basins = []

    for low in lows:
        # print("-"*20)
        # print(low)
        basins.append(findBasin(hm, low))

    top3 = [0, 0, 0]

    for basin in basins:
        basinSize = len(basin)

        if basinSize > top3[2]:
            top3[0] = top3[1]
            top3[1] = top3[2]
            top3[2] = basinSize
        elif basinSize > top3[1]:
            top3[0] = top3[1]
            top3[1] = basinSize
        elif basinSize > top3[0]:
            top3[0] = basinSize

    print(top3[0] * top3[1] * top3[2])


def findLows(hm):
    lows = []

    # assume quadratic hm
    rowCount = len(hm)
    colCount = len(hm[0])

    for r in range(rowCount):
        for c in range(colCount):
            h = hm[r][c]

            if r == 0:
                if c == 0:
                    # top left --> check south and east
                    isLow = h < hm[r+1][c] and h < hm[r][c+1]
                elif c == colCount-1:
                    # top right --> check south and west
                    isLow = h < hm[r+1][c] and h < hm[r][c-1]
                else:
                    # top row --> check south and east and west
                    # autopep8:off
                    isLow = h < hm[r+1][c] and h < hm[r][c+1] and h < hm[r][c-1]
                    # autopep8:on
            elif r == rowCount-1:
                if c == 0:
                    # bottom left --> check north and east
                    isLow = h < hm[r-1][c] and h < hm[r][c+1]
                elif c == colCount-1:
                    # bottom right --> check north and west
                    isLow = h < hm[r-1][c] and h < hm[r][c-1]
                else:
                    # bottom row --> check north and east and west
                    # autopep8:off
                    isLow = h < hm[r-1][c] and h < hm[r][c+1] and h < hm[r][c-1]
                    # autopep8:on
            else:
                # north and south
                isLow = h < hm[r-1][c] and h < hm[r+1][c]

                # west
                if c > 0:
                    isLow = isLow and h < hm[r][c-1]

                # east
                if c < colCount-1:
                    isLow = isLow and h < hm[r][c+1]

            if isLow:
                lows.append((r, c))
    return lows


def findBasin(hm, low: Tuple[int, int]) -> List[Tuple[int, int]]:
    basin = {}
    unvisited = [low]

    while len(unvisited) > 0:
        curPos = unvisited.pop()

        try:
            basin[curPos[0]].add(curPos[1])
        except KeyError:
            basin.update({curPos[0]: set([curPos[1]])})

        # search around current position
        # autopep8:off
        n = None if curPos[0] == 0 else (curPos[0]-1, curPos[1])
        e = None if curPos[1] == len(hm[curPos[0]])-1 else (curPos[0], curPos[1]+1)
        s = None if curPos[0] == len(hm)-1 else (curPos[0]+1, curPos[1])
        w = None if curPos[1] == 0 else (curPos[0], curPos[1]-1)
        # autopep8:on

        # add valid and unvisited positions to the queue
        for newPos in [n, e, s, w]:
            if newPos:
                if newPos[0] in basin.keys() and newPos[1] in basin[newPos[0]]:
                    continue
                if hm[newPos[0]][newPos[1]] == 9:
                    continue

                unvisited.append(newPos)

    basinList = []
    for r in basin:
        basinList.extend((r, c) for c in basin[r])

    return basinList


if __name__ == "__main__":
    star1()
    star2()
