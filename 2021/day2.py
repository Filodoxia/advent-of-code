from enum import Enum
import input as inp


class Position():
    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y

    def __str__(self) -> str:
        return f"""({self.x},{self.y})"""


class Submarine():
    def __init__(self, position: Position, aim: int) -> None:
        self.position = position
        self.aim = aim

    def __str__(self) -> str:
        return f"""Position: ({self.position.x},{self.position.y}), Aim: {self.aim}"""


class Direction(Enum):
    UP = 1
    DOWN = 2
    FORWARD = 3


DIRECTION_MAP = {
    "forward": Direction.FORWARD,
    "down": Direction.DOWN,
    "up": Direction.UP
}


class Instruction():
    direction: Direction
    distance: int

    def __init__(self, direction: Direction, distance: int) -> None:
        self.direction = direction
        self.distance = distance

    def __str__(self) -> str:
        return f"""{self.direction}, {self.distance}"""


def parseInstruction(instruction: str) -> Instruction:
    instr = instruction.split(" ")
    return Instruction(DIRECTION_MAP[instr[0]], int(instr[1]))


def executeInstruction1(position: Position, instruction: Instruction) -> None:
    if instruction.direction == Direction.FORWARD:
        position.x += instruction.distance
    elif instruction.direction == Direction.UP:
        position.y -= instruction.distance
    elif instruction.direction == Direction.DOWN:
        position.y += instruction.distance


def executeInstruction2(sub: Submarine, instruction: Instruction) -> None:
    if instruction.direction == Direction.FORWARD:
        sub.position.x += instruction.distance
        sub.position.y += instruction.distance * sub.aim
    elif instruction.direction == Direction.UP:
        sub.aim -= instruction.distance
    elif instruction.direction == Direction.DOWN:
        sub.aim += instruction.distance


def star1():
    pos = Position(0, 0)

    with inp.read(2) as input:
        for line in input:
            instr = parseInstruction(line)
            executeInstruction1(pos, instr)

    print(f"""Final position: {pos}""")
    print(pos.x * pos.y)


def star2():
    sub = Submarine(Position(0, 0), 0)

    with inp.read(2) as input:
        for line in input:
            instr = parseInstruction(line)
            executeInstruction2(sub, instr)

    print(sub)
    print(sub.position.x * sub.position.y)


if __name__ == "__main__":
    star1()
    star2()
