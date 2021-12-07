from typing import List, Tuple
from math import sqrt
import input as inp


class BingoCard():
    card: List[int]
    bingo: bool
    dimension: int
    # tracks the drawn numbers
    draws: List[int]
    # hits tracks the number of hits per potential bingo line
    # first element = #hits in the first row,
    # second element = #hits in the second row, ...
    # (dimension+1)st element = #hits in the first column, ...
    hits: List[int]
    # keep track of the sum of unmarked numbers for the score
    # because otherwise it's a bit annoying to calculate when bingo is achieved and the score is requested
    unmarkedSum: int

    def __init__(self, card: List[int]) -> None:
        d = sqrt(len(card))
        if not d == int(d):
            raise Exception(
                f"""Board must be sqare but {len(card)} numbers cannot make a square""")
        self.dimension = int(d)
        self.card = card
        self.unmarkedSum = sum(card)
        # rows = #columns = dimension of card => 2*d bingo lines
        self.hits = [0]*(int(2*self.dimension))
        self.draws = []
        self.bingo = False

    def _cardIndexToPosition(self, listIndex: int) -> Tuple[int, int]:
        """
        Transforms the index in the card list to the row/column position.
        List index is 0,...,(2*dimension)-1
        Position indicates row/column on the card, i.e. (1,1),...(dimension,dimension)
        """
        # row is floor division + 1:
        # row 1: list indices 0,...,d-1 => 0+1=1
        # row 2: list indices d,...,2d-1 => 1+1=2
        # row d: list indices (d-1)d,...,dd-1 => d-1+1=d
        row = (listIndex // self.dimension) + 1
        column = (listIndex % self.dimension) + 1
        return (row, column)

    def mark(self, number: int) -> None:
        for i in range(len(self.card)):
            # print(self.card[i], number)

            if self.card[i] == number:
                self.unmarkedSum -= number
                row, column = self._cardIndexToPosition(i)

                self.hits[row-1] += 1
                if self.hits[row-1] == self.dimension:
                    self.bingo = True

                colIndex = self.dimension + column - 1
                self.hits[colIndex] += 1
                if self.hits[colIndex] == self.dimension:
                    self.bingo = True

        self.draws.append(number)

    def score(self) -> int:
        if len(self.draws) < self.dimension or not self.bingo:
            return 0

        return self.unmarkedSum*self.draws[-1]


def prepGame() -> Tuple[List[BingoCard], List[int]]:
    cards: List[BingoCard] = []

    with inp.read(4) as input:
        # read draw sequence and skip the following empty line
        draws = list(map(int, input.readline().split(",")))
        next(input)

        card: List[int] = []
        for line in input:
            if line == "\n":
                # on empty line create a new card with the numbers read so far,
                # add it to the card list and reset the list that holds numbers
                # and continue with the next line
                cards.append(BingoCard(card))
                card = []
                continue

            numbers = line.split(" ")
            numbers[-1] = numbers[-1].strip()

            for n in numbers:
                if n == "":
                    # skip empty elements that happen when formatting single digit numbers,
                    # e.g. "14  2" is split into ["14","","2"]
                    continue
                card.append(int(n))

        # make sure the last card is added as well
        cards.append(BingoCard(card))

    return (cards, draws)


def star1():
    cards, draws = prepGame()
    winners = playBingo(cards, draws)
    print([w.score() for w in winners])


def star2():
    cards, draws = prepGame()
    loser = loseBingo(cards, draws)
    print(loser.score())


def playBingo(cards: List[BingoCard], draws: List[int]) -> List[BingoCard]:
    # to account for potentially multiple winners in the same round
    winners: List[BingoCard] = []
    isBingoRound = False

    for n in draws:
        for card in cards:
            card.mark(n)

            if card.bingo:
                isBingoRound = True
                winners.append(card)

        if isBingoRound:
            return winners

    return winners


def loseBingo(cards: List[BingoCard], draws: List[int]):
    bingoCount = 0

    for n in draws:
        for card in cards:
            hadBingo = card.bingo
            card.mark(n)

            if (not hadBingo) and card.bingo:
                bingoCount += 1
                if bingoCount == len(cards):
                    return card

    return None


if __name__ == "__main__":
    star1()
    star2()
