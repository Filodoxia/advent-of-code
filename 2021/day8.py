from typing import List
import input as inp
from enum import IntEnum


class Segments(IntEnum):
    a = 1,   # 00000001
    b = 2,   # 00000010
    c = 4,   # 00000100
    d = 8,   # 00001000
    e = 16,  # 00010000
    f = 32,  # 00100000
    g = 64   # 01000000


PATTERN_SUM_MAP = {
    sum([Segments[s] for s in "abcefg"]): 0,
    sum([Segments[s] for s in "cf"]): 1,
    sum([Segments[s] for s in "acdeg"]): 2,
    sum([Segments[s] for s in "acdfg"]): 3,
    sum([Segments[s] for s in "bcdf"]): 4,
    sum([Segments[s] for s in "abdfg"]): 5,
    sum([Segments[s] for s in "abdefg"]): 6,
    sum([Segments[s] for s in "acf"]): 7,
    sum([Segments[s] for s in "abcdefg"]): 8,
    sum([Segments[s] for s in "abcdfg"]): 9
}


def star1():
    digitCount = [0]*10

    with inp.read(8) as input:
        for line in input:
            a = line.split("|")
            output = processLine(
                a[0].strip().split(" "),
                a[1].strip().split(" ")
            )

            for value in output:
                digitCount[value] += 1

    print(digitCount[1]+digitCount[4]+digitCount[7]+digitCount[8])


def star2():
    sum = 0

    with inp.read(8) as input:
        for line in input:
            a = line.split("|")
            output = processLine(
                a[0].strip().split(" "),
                a[1].strip().split(" ")
            )
            sum += int("".join(map(str, output)))

    print(sum)


def processLine(signalPatterns: List[str], outputValues: List[str]) -> List:
    parsedOutput = []

    patterns = {
        "1": [p for p in signalPatterns if len(p) == 2][0],
        "4": [p for p in signalPatterns if len(p) == 4][0],
        "7": [p for p in signalPatterns if len(p) == 3][0],
        "8": [p for p in signalPatterns if len(p) == 7][0]
    }

    missingOneSegment = [s for s in signalPatterns if len(s) == 6]
    missingTwoSegments = [s for s in signalPatterns if len(s) == 5]

    wireToSegmentMap = {}

    cf = set(list(patterns["1"]))
    bd = set(list(patterns["4"])).difference(cf)
    a = set(list(patterns["7"])).difference(cf)

    # intersection of the "missing two" patterns
    adg = set(list(missingTwoSegments[0])).intersection(
        list(missingTwoSegments[1])).intersection(list(missingTwoSegments[2]))

    dg = adg.difference(a)
    d = dg.intersection(bd)
    g = dg.difference(d)

    # intersection of the "missing one" patterns
    abfg = set(list(missingOneSegment[0])).intersection(
        list(missingOneSegment[1])).intersection(list(missingOneSegment[2]))

    bf = abfg.difference(a).difference(g)
    f = bf.intersection(list(patterns["1"]))
    b = bf.difference(f)
    c = cf.difference(f)
    e = set(list(patterns["8"])).difference(abfg).difference(c).difference(d)

    wireToSegmentMap[a.pop()] = Segments.a
    wireToSegmentMap[b.pop()] = Segments.b
    wireToSegmentMap[c.pop()] = Segments.c
    wireToSegmentMap[d.pop()] = Segments.d
    wireToSegmentMap[e.pop()] = Segments.e
    wireToSegmentMap[f.pop()] = Segments.f
    wireToSegmentMap[g.pop()] = Segments.g

    for outVal in outputValues:
        patternSum = sum([wireToSegmentMap[w] for w in list(outVal)])
        parsedOutput.append(PATTERN_SUM_MAP[patternSum])

    return parsedOutput


if __name__ == "__main__":
    star1()
    star2()
