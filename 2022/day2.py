from enum import Enum
import input


class Shape(Enum):
    ROCK = "rock",
    PAPER = "paper",
    SCISSOR = "scissor"


class RoundResult(Enum):
    WIN = "win",
    DRAW = "draw",
    LOSS = "loss"


SCORES: dict[Shape | RoundResult, int] = {
    RoundResult.LOSS: 0,
    RoundResult.DRAW: 3,
    RoundResult.WIN: 6,
    Shape.SCISSOR: 3,
    Shape.PAPER: 2,
    Shape.ROCK: 1,
}

MATCH_RESULT_MAP: dict[tuple[Shape, Shape], RoundResult] = {
    (Shape.ROCK, Shape.ROCK): RoundResult.DRAW,
    (Shape.ROCK, Shape.PAPER): RoundResult.WIN,
    (Shape.ROCK, Shape.SCISSOR): RoundResult.LOSS,
    (Shape.PAPER, Shape.ROCK): RoundResult.LOSS,
    (Shape.PAPER, Shape.PAPER): RoundResult.DRAW,
    (Shape.PAPER, Shape.SCISSOR): RoundResult.WIN,
    (Shape.SCISSOR, Shape.ROCK): RoundResult.WIN,
    (Shape.SCISSOR, Shape.PAPER): RoundResult.LOSS,
    (Shape.SCISSOR, Shape.SCISSOR): RoundResult.DRAW
}

INPUT_SHAPE_MAP = {
    "A": Shape.ROCK,
    "B": Shape.PAPER,
    "C": Shape.SCISSOR,
    "X": Shape.ROCK,
    "Y": Shape.PAPER,
    "Z": Shape.SCISSOR
}

INPUT_REQUIRED_RESULT_MAP = {
    "X": RoundResult.LOSS,
    "Y": RoundResult.DRAW,
    "Z": RoundResult.WIN
}


DESIRED_RESULT_MAP: dict[tuple[Shape, RoundResult], Shape] = {
    (Shape.ROCK, RoundResult.WIN): Shape.PAPER,
    (Shape.ROCK, RoundResult.DRAW): Shape.ROCK,
    (Shape.ROCK, RoundResult.LOSS): Shape.SCISSOR,
    (Shape.PAPER, RoundResult.WIN): Shape.SCISSOR,
    (Shape.PAPER, RoundResult.DRAW): Shape.PAPER,
    (Shape.PAPER, RoundResult.LOSS): Shape.ROCK,
    (Shape.SCISSOR, RoundResult.WIN): Shape.ROCK,
    (Shape.SCISSOR, RoundResult.DRAW): Shape.SCISSOR,
    (Shape.SCISSOR, RoundResult.LOSS): Shape.PAPER
}


def star1():
    matches = input.readLines("day2.txt")
    score = 0

    for match in matches:
        opponentShape = Shape(INPUT_SHAPE_MAP[match[0]])
        myShape = Shape(INPUT_SHAPE_MAP[match[2]])
        matchResult = MATCH_RESULT_MAP[(opponentShape, myShape)]
        score += SCORES[matchResult] + SCORES[myShape]

    return score


def star2():
    matches = input.readLines("day2.txt")
    score = 0

    for match in matches:
        opponentShape = Shape(INPUT_SHAPE_MAP[match[0]])
        requiredResult = INPUT_REQUIRED_RESULT_MAP[match[2]]
        myShape = DESIRED_RESULT_MAP[(opponentShape, requiredResult)]
        matchResult = MATCH_RESULT_MAP[(opponentShape, myShape)]
        score += SCORES[matchResult] + SCORES[myShape]

    return score


if __name__ == "__main__":
    print(star1())
    print(star2())
