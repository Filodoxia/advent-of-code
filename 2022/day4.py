import input


def star1():
    inp = input.readLines("day4.txt")
    fullyContainedCount = 0

    for line in inp:
        pair = line.split(",")
        range1 = list(map(lambda x: int(x), pair[0].split("-")))
        range2 = list(map(lambda x: int(x), pair[1].split("-")))

        startsFirstRange1 = range1[0] <= range2[0]
        startsFirstRange2 = range2[0] <= range1[0]
        endsFirstRange1 = range1[1] <= range2[1]
        endsFirstRange2 = range2[1] <= range1[1]

        if (startsFirstRange1 and endsFirstRange2) or (startsFirstRange2 and endsFirstRange1):
            fullyContainedCount += 1

    return fullyContainedCount


def star2():
    inp = input.readLines("day4.txt")
    overlapCount = 0

    for line in inp:
        pair = line.split(",")
        range1 = list(map(lambda x: int(x), pair[0].split("-")))
        range2 = list(map(lambda x: int(x), pair[1].split("-")))

        startsFirstRange1 = range1[0] <= range2[0]
        startsFirstRange2 = range2[0] <= range1[0]
        start1beforeEnd2 = range1[0] <= range2[1]
        start2beforeEnd1 = range2[0] <= range1[1]

        if (startsFirstRange1 and start2beforeEnd1) or (startsFirstRange2 and start1beforeEnd2):
            overlapCount += 1

    return overlapCount


if __name__ == "__main__":
    print(star1())
    print(star2())
