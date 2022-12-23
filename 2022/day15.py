from dataclasses import dataclass
import input
import re


DAY = 15
TEST1 = False
TEST2 = False
DEBUG1 = False
DEBUG2 = False

INPUT_REGEX = re.compile(".*x=(-?\d+), y=(-?\d+).*x=(-?\d+), y=(-?\d+)")


def getInput(part: int):
    filename = f"""day{DAY}{"_test" if (TEST1 if part==1 else TEST2) else ""}.txt"""
    return input.readLines(filename)


def star1():
    yTest = 2_000_000
    blockedPositions = set()
    beaconPosInTestRow = set()

    for line in getInput(1):
        rgex = INPUT_REGEX.match(line)

        sensorX = int(rgex.group(1))
        sensorY = int(rgex.group(2))
        beaconX = int(rgex.group(3))
        beaconY = int(rgex.group(4))

        if beaconY == yTest:
            beaconPosInTestRow.add(beaconX)

        distBeacon = abs(beaconX-sensorX) + abs(beaconY-sensorY)
        dist = abs(yTest-sensorY)

        if dist < distBeacon:
            distDiff = distBeacon - dist
            x = [x for x in range(sensorX-distDiff, sensorX+distDiff+1)]
            blockedPositions.update(x)

    blockedPositions.difference_update(beaconPosInTestRow)

    return f"Star 1:{len(blockedPositions)}"


@dataclass
class Sensor():
    x: int
    y: int
    r: int


def manhattan(a: tuple[int, int], b: tuple[int, int]) -> int:
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def star2():
    n = 4_000_000  # 20
    sensors: list[Sensor] = []
    border = [0] * (n+1)

    for line in getInput(2):
        rgex = INPUT_REGEX.match(line)

        sensorX = int(rgex.group(1))
        sensorY = int(rgex.group(2))
        beaconX = int(rgex.group(3))
        beaconY = int(rgex.group(4))
        r = manhattan((sensorX, sensorY), (beaconX, beaconY))

        sensors.append(Sensor(sensorX, sensorY, r))

    sensors.sort(key=lambda s: s.x)

    for s in sensors:
        yTop = max(s.y - s.r, 0)
        yBot = min(s.y + s.r, n)

        if DEBUG2:
            print(s)

        for y in range(yTop, yBot+1):
            xL = s.x - (s.r - abs(s.y - y))
            xR = s.x + (s.r - abs(s.y - y))

            if xL <= border[y]+1 and xR > border[y]:
                border[y] = xR

        if DEBUG2:
            print(border)

    for k, v in enumerate(border):
        if v < n:
            if DEBUG2:
                print(v+1, k)
            freq = ((v+1)*4_000_000) + k
    return f"Star 2: {freq}"


if __name__ == "__main__":
    print(star1())
    print(star2())
