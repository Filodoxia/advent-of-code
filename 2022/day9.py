from enum import Enum
import input


def star1():
    return executeProgram("day9.txt", 2, False)


def star2():
    return executeProgram("day9.txt", 10, False)


def executeProgram(program: str, knotCount: int, debug: bool = False):
    rope = Rope(knotCount)
    if debug:
        rope.printPositions()

    for cmd in input.readLines(program):
        direction = Direction(cmd[0])

        if debug:
            print(f"===== {cmd} =====")

        rope.move(direction, int(cmd[2:]), debug)

        if debug:
            rope.printPositions()

    if debug:
        print(f"Tail's visited positions: {rope.knots[-1].visitedPositions}")
    return rope.knots[-1].visitedPostionCount()


class Direction(Enum):
    UP = "U"
    DOWN = "D"
    LEFT = "L"
    RIGHT = "R"
    UPRIGHT = "UL"
    UPLEFT = "UR"
    DOWNRIGHT = "DR"
    DOWNLEFT = "DL"


class RopeElement():
    def __init__(self, name: str) -> None:
        self.visitedPositions: dict[int, set[int]] = {0: set([0])}
        self.x: int = 0
        self.y: int = 0
        self.nextElement: RopeElement | None = None
        self.name = name

    def visitedPostionCount(self) -> int:
        return sum(map(len, self.visitedPositions.values()))

    def move(self, direction: Direction, debug: bool = False):
        if debug:
            print(f"moving {self.name} {direction}")

        if direction == Direction.UP:
            self.y += 1
        elif direction == Direction.DOWN:
            self.y -= 1
        elif direction == Direction.LEFT:
            self.x -= 1
        elif direction == Direction.RIGHT:
            self.x += 1
        elif direction == Direction.UPLEFT:
            self.x -= 1
            self.y += 1
        elif direction == Direction.UPRIGHT:
            self.x += 1
            self.y += 1
        elif direction == Direction.DOWNRIGHT:
            self.x += 1
            self.y -= 1
        elif direction == Direction.DOWNLEFT:
            self.x -= 1
            self.y -= 1

        if self.nextElement:
            xDiff = self.x - self.nextElement.x
            yDiff = self.y - self.nextElement.y

            if abs(xDiff) == 2 or abs(yDiff) == 2:
                followDiagonally = not ((xDiff == 0) or (yDiff == 0))
                if debug:
                    print(f"follow Diag: {followDiagonally} ({xDiff},{yDiff})")

                if followDiagonally:
                    if xDiff < 0 and yDiff > 0:
                        followDirection = Direction.UPLEFT
                    elif xDiff > 0 and yDiff > 0:
                        followDirection = Direction.UPRIGHT
                    elif xDiff > 0 and yDiff < 0:
                        followDirection = Direction.DOWNRIGHT
                    else:
                        followDirection = Direction.DOWNLEFT
                else:
                    if xDiff == -2:
                        followDirection = Direction.LEFT
                    elif xDiff == 2:
                        followDirection = Direction.RIGHT
                    elif yDiff == 2:
                        followDirection = Direction.UP
                    else:
                        followDirection = Direction.DOWN

                self.nextElement.move(followDirection, debug)

        self.visitedPositions.setdefault(self.x, set([self.y]))
        self.visitedPositions[self.x].add(self.y)


class Rope():
    def __init__(self, knotCount: int = 2) -> None:
        self.head = RopeElement("head")
        self.knots = [self.head]

        for i in range(knotCount-1):
            self.knots.append(RopeElement(f"{i+1}"))
            self.knots[-2].nextElement = self.knots[-1]

    def move(self, direction: Direction, distance: int, debug: bool = False):
        for _ in range(distance):
            self.head.move(direction, debug)

    def printPositions(self):
        for knot in self.knots:
            print(knot.x, knot.y, f"({knot.name})")


if __name__ == "__main__":
    print(star1())
    print(star2())
