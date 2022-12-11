from dataclasses import dataclass
from functools import reduce
import re

import input


DEBUG: bool = False
RING_MODULO: int = 0
MONKEY_REGEX = re.compile(
    "Monkey (\d*):\n  Starting items: (\d*[, \d*]*)\n  Operation: new = (.*)\n  Test: divisible by (\d*)\n    If true: throw to monkey (\d*)\n    If false: throw to monkey (\d*)")


@dataclass()
class Test():
    divisor: int
    targetTrue: int
    targetFalse: int


class Monkey():
    def __init__(self, name: int, startingItems: list[int], operation: str, test: Test) -> None:
        self.name = name
        self.items = startingItems
        self.operation = operation
        self.test = test
        self.inspectedItems = 0

    def inspect(self, divideByThree: bool = False) -> list[tuple[int, int]]:
        inspResut: list[tuple[int, int]] = []
        for item in self.items:
            old = item
            new = eval(self.operation)
            if divideByThree:
                new = new // 3

            if new < 0:
                raise Exception()

            if new % self.test.divisor:
                targetMonkey = self.test.targetFalse
            else:
                targetMonkey = self.test.targetTrue

            if RING_MODULO:
                new = new % RING_MODULO

            self.inspectedItems += 1
            inspResut.append((targetMonkey, new))
        self.items = []
        return inspResut

    def __str__(self) -> str:
        return (
            f"Monkey: {self.name:2}:\n"
            f"  items:     {self.items}\n"
            f"  operation: {self.operation}\n"
            f"  test:      {repr(self.test)}\n"
            f"  inspected: {self.inspectedItems}"
        )


def simulate(rounds: int, divideByThree: bool = False):
    monkeys: dict[int, Monkey] = {}

    for mk in input.read("day11.txt").split("\n\n"):
        r = MONKEY_REGEX.match(mk).groups()
        m = Monkey(
            name=int(r[0]),
            startingItems=list(map(int, r[1].split(","))),
            operation=r[2],
            test=Test(int(r[3]), int(r[4]), int(r[5]))
        )
        monkeys.update({m.name: m})

    # set ring modulo
    global RING_MODULO
    # RING_MODULO = 96577  # modulo for part 1
    RING_MODULO = reduce(
        lambda x, y: x*y, [m.test.divisor for m in monkeys.values()])
    if DEBUG:
        print(RING_MODULO)

    # 20 inspection rounds
    for round in range(rounds):
        for mk in monkeys.values():
            for targetMonkey, item in mk.inspect(divideByThree):
                monkeys[targetMonkey].items.append(item)

        if DEBUG:
            print(f"\n===== Round {round+1:2} =====")
            for mk in monkeys.values():
                print(f"Monkey {mk.name}: {mk.items}")

    inspCounts = sorted([m.inspectedItems for m in monkeys.values()])
    if DEBUG:
        print(f"Inspection counts: {inspCounts}")

    return inspCounts[-1]*inspCounts[-2]


def star1():
    return simulate(20, True)


def star2():
    return simulate(10_000, False)


if __name__ == "__main__":
    DEBUG = True
    print(star1())
    DEBUG = False
    print(star2())
