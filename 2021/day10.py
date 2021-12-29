from __future__ import annotations
from typing import List, Literal, Tuple
import input as inp

SYMBOL_PAIRS = {"(": ")", "[": "]", "{": "}", "<": ">"}
OPENING_SYMBOLS = ["(", "[", "{", "<"]
CLOSING_SYMBOLS = [")", "]", "}", ">"]


class CorruptChunkException(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)


class IncompleteChunkException(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)


class Chunk():
    children: List[Chunk]
    parent: Chunk
    closed: bool
    symbol: Literal["(", "[", "{", "<"]

    def __init__(self, symbol: Literal["(", "[", "{", "<"], parentChunk: Chunk):
        self.children = []
        self.parent = parentChunk
        self.closed = False
        self.symbol = symbol


class NavLine():
    roots: List[Chunk]
    corrupted: bool
    incomplete: bool
    activeChunk: Chunk
    illegalCharacter: str

    def __init__(self):
        self.roots = []
        self.corrupted = False
        self.incomplete = False
        self.activeChunk = None
        self.illegalCharacter = None

    def open(self, symbol: Literal["(", "[", "{", "<"]):
        if symbol not in OPENING_SYMBOLS:
            raise Exception("Wrong symbol")

        newChunk = Chunk(symbol, self.activeChunk)
        if self.activeChunk:
            self.activeChunk.children.append(newChunk)
        else:
            self.roots.append(newChunk)
        self.activeChunk = newChunk

    def close(self, symbol: Literal[")", "]", "}", ">"]):
        if symbol not in CLOSING_SYMBOLS:
            raise Exception("Wrong symbol")

        if not symbol == SYMBOL_PAIRS[self.activeChunk.symbol]:
            self.corrupted = True
            self.illegalCharacter = symbol
            raise CorruptChunkException(
                f"""Wrong closing symbol (expected "{self.activeChunk.symbol}", got "{symbol}")""")

        self.activeChunk.closed = True
        self.activeChunk = self.activeChunk.parent

    def parse(self, line: str):
        for symbol in line:
            if symbol in OPENING_SYMBOLS:
                self.open(symbol)
            else:
                try:
                    self.close(symbol)
                except CorruptChunkException:
                    self.corrupted = True
                    return

        self.incomplete = self._checkForIncomplete()

    def _checkForIncomplete(self):
        return not self.activeChunk.closed

    def complete(self) -> str:
        if not self.incomplete:
            return ""

        completionSequence = ""
        c = self.activeChunk
        while c:
            completionSequence += SYMBOL_PAIRS[c.symbol]
            c = c.parent

        return completionSequence


def star1():
    SCORES = {
        ")": 3,
        "]": 57,
        "}": 1197,
        ">": 25137
    }
    errorScore = 0

    for line in inp.read(10):
        print(line.strip())
        nl = NavLine()
        nl.parse(line.strip())

        if nl.corrupted:
            errorScore += SCORES[nl.illegalCharacter]

        print(f"""Incomplete: {nl.incomplete}, Corrupted: {nl.corrupted}\n""")

    print(f"""Error score: {errorScore}""")


def star2():
    SCORES = {
        ")": 1,
        "]": 2,
        "}": 3,
        ">": 4
    }
    MULTIPLIER = 5
    incompleteLines: List[NavLine] = []
    completionSequences: List[str] = []

    for line in inp.read(10):
        nl = NavLine()
        nl.parse(line.strip())

        if nl.incomplete:
            incompleteLines.append(nl)

    for line in incompleteLines:
        complStr = line.complete()
        score = 0

        for symbol in complStr:
            score *= MULTIPLIER
            score += SCORES[symbol]

        completionSequences.append((complStr, score))

    completionSequences.sort(key=lambda x: x[1])

    print(completionSequences)
    medianScore = completionSequences[int(len(completionSequences)/2)]
    print(f"""Median score of completion: {medianScore}""")


if __name__ == "__main__":
    star1()
    star2()
