import input


def star1():
    forrest = input.readGrid("day8.txt")
    n = len(forrest)
    visibilityMap = getVisibilityMap(forrest)
    visibleCount = 0
    for r in range(n):
        for c in range(n):
            visibleCount += 1 if visibilityMap[r][c] else 0
    return visibleCount


def star2():
    forrest = input.readGrid("day8.txt")
    scores = getScenicScores(forrest)
    return max([max(x) for x in scores])


def getScenicScores(forrest: list[list[int]]) -> list[list[int]]:
    scores = []
    n = len(forrest)

    for rowIndex, row in enumerate(forrest):
        rowScores = []
        for colIndex, currentTreeHeight in enumerate(row):
            # initial view distances
            vdNorth = 0
            vdEast = 0
            vdSouth = 0
            vdWest = 0

            # search north
            for r in range(rowIndex-1, -1, -1):
                vdNorth += 1
                if forrest[r][colIndex] >= currentTreeHeight:
                    break

            # search east
            for c in range(colIndex+1, n):
                vdEast += 1
                if forrest[rowIndex][c] >= currentTreeHeight:
                    break

            # search south
            for r in range(rowIndex+1, n):
                vdSouth += 1
                if forrest[r][colIndex] >= currentTreeHeight:
                    break

            # search west
            for c in range(colIndex-1, -1, -1):
                vdWest += 1
                if forrest[rowIndex][c] >= currentTreeHeight:
                    break

            rowScores.append(vdNorth*vdEast*vdSouth*vdWest)

        scores.append(rowScores)
    return scores


def getVisibilityMap(forrest: list[list[int]]) -> list[list[bool]]:
    n = len(forrest)

    visibilityMap: list[list[bool]] = []
    for row in range(n):
        # first and last row are visible by default because
        # they dont even have trees all around
        if row == 0 or row == n-1:
            visibilityMap.append([True]*n)
            continue

        rowVisibility: list[bool] = []
        for col in range(n):
            # trees in first and last column are always visible
            if col == 0 or col == n-1:
                rowVisibility.append(True)
                continue

            visibleNorth = True
            visibleEast = True
            visibleSouth = True
            visibleWest = True

            # check row for covering trees
            for c in range(0, col):
                if forrest[row][col] <= forrest[row][c]:
                    visibleWest = False
                    break

            # if visible other directions need not be checked and next tree can be checked
            if visibleWest:
                rowVisibility.append(True)
                continue

            # check row for covering trees
            for c in range(col+1, n):
                if forrest[row][col] <= forrest[row][c]:
                    visibleEast = False
                    break

            # if visible other directions need not be checked and next tree can be checked
            if visibleEast:
                rowVisibility.append(True)
                continue

            # check column for covering trees
            for r in range(0, row):
                if forrest[row][col] <= forrest[r][col]:
                    visibleNorth = False
                    break

            # if visible other directions need not be checked and next tree can be checked
            if visibleNorth:
                rowVisibility.append(True)
                continue

            # check column for covering trees
            for r in range(row+1, n):
                if forrest[row][col] <= forrest[r][col]:
                    visibleSouth = False
                    break

            # if still not visible, then the tree is not visible from any direction
            if visibleSouth:
                rowVisibility.append(True)
            else:
                rowVisibility.append(False)

        visibilityMap.append(rowVisibility)

    return visibilityMap


if __name__ == "__main__":
    print(star1())
    print(star2())
