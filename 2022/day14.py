from enum import Enum
import input

DAY = 14
TEST1 = False
TEST2 = False
DEBUG1 = False
DEBUG2 = False


class FallDirection(Enum):
    NO_FALL = 0
    DOWN = 1
    LEFT = 2
    RIGHT = 3


def getInput(part: int) -> list[list[tuple[int, int]]]:
    filename = f"""day{DAY}{"_test" if (TEST1 if part==1 else TEST2) else ""}.txt"""
    return [[tuple(map(int, p.split(","))) for p in l.split("->")] for l in input.readLines(filename)]


def getRockCoordinates(input: list[list[tuple[int, int]]]):
    rc: dict[int, set[int]] = {}

    for line in input:
        for i in range(len(line)-1):
            start = line[i]
            end = line[i+1]

            if start[0] > end[0] or start[1] > end[1]:
                start = line[i+1]
                end = line[i]

            for x in range(start[0], end[0]+1):
                for y in range(start[1], end[1]+1):
                    rc.setdefault(x, set())
                    rc[x].add(y)

    return rc


def getFallDirection(rc: dict[int, set[int]], pos: tuple[int, int], debug: bool) -> tuple[FallDirection, tuple[int, int]]:
    newY = pos[1]+1

    # test below
    if newY not in rc.setdefault(pos[0], set()):
        if debug:
            print("Fall down")
        return FallDirection.DOWN, (pos[0], newY)
    # test left below
    elif newY not in rc.setdefault(pos[0]-1, set()):
        if debug:
            print("Fall down left")
        return FallDirection.LEFT, (pos[0]-1, newY)
    # test right below
    elif newY not in rc.setdefault(pos[0]+1, set()):
        if debug:
            print("Fall down right")
        return FallDirection.RIGHT, (pos[0]+1, newY)

    if debug:
        print("Cant fall")
    return FallDirection.NO_FALL, pos


def star1():
    sandCount, sandStartPos = 0, (500, 0)

    rc = getRockCoordinates(getInput(1))
    maxY = max([max(y) for y in rc.values()])

    if DEBUG1:
        print("Rock coordinates:")
        print(rc)
        print("\nSimulating sand\n---------------")

    cameToRest = True

    while cameToRest:
        sandCount += 1
        curPos = sandStartPos
        cameToRest = False

        if DEBUG1:
            print("\nNew sand unit")

        # simulate falling
        while not cameToRest:
            if curPos[1] > maxY:
                return f"Star 1: {sandCount-1}"

            fd, curPos = getFallDirection(rc, curPos, DEBUG1)
            if fd == FallDirection.DOWN:
                cameToRest = False
            elif fd == FallDirection.LEFT:
                cameToRest = False
            elif fd == FallDirection.RIGHT:
                cameToRest = False
            elif fd == FallDirection.NO_FALL:
                # add sand unit to rc to block further units
                rc.setdefault(curPos[0], set()).add(curPos[1])
                cameToRest = True

    return f"Star 1: Failed"


def star2():
    sandCount, sandStartPos = 0, (500, 0)

    rc = getRockCoordinates(getInput(2))
    # make sure sandStartPos column is in rc because we always check it
    rc.setdefault(sandStartPos[0], set())
    floorY = max([max(y) for y in rc.values()])+2

    if DEBUG2:
        print("Rock coordinates:")
        print(rc)
        print("\nSimulating sand\n---------------")

    cameToRest = True

    while cameToRest:
        if sandStartPos[1] in rc[sandStartPos[0]]:
            return f"Start 2: {sandCount}"

        sandCount += 1
        curPos = sandStartPos
        cameToRest = False

        if DEBUG2:
            print("\nNew sand unit")

        # simulate falling
        while not cameToRest:
            # cant fall into floor level
            if curPos[1]+1 == floorY:
                # add sand unit to rc to block further units
                rc.setdefault(curPos[0], set()).add(curPos[1])
                cameToRest = True
                break

            fd, curPos = getFallDirection(rc, curPos, DEBUG2)

            if fd == FallDirection.DOWN:
                cameToRest = False
            elif fd == FallDirection.LEFT:
                cameToRest = False
            elif fd == FallDirection.RIGHT:
                cameToRest = False
            elif fd == FallDirection.NO_FALL:
                # add sand unit to rc to block further units
                rc.setdefault(curPos[0], set()).add(curPos[1])
                cameToRest = True

    return f"Star 2: Failed"


if __name__ == "__main__":
    print(star1())
    print(star2())
