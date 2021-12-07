from io import TextIOWrapper
from typing import Iterable, List, Tuple
import input as inp
from math import ceil


class AnalysisResult():
    lineLength: int
    numberOfLines: int
    frequencyOfZero: Tuple[int, ...]

    def __init__(self, lineLength: int, numberOfLines: int, frequencyOfZero: Iterable) -> None:
        self.lineLength = lineLength
        self.numberOfLines = numberOfLines
        self.frequencyOfZero = tuple(frequencyOfZero)

        if not len(self.frequencyOfZero) == self.lineLength:
            errMsg = f"""frequencyOfZero iterable has the wrong length (expected {self.lineLength} but got {len(self.frequencyOfZero)})"""
            raise Exception(errMsg)


def analyzeReport(numbers: List[str], lineLength: int) -> AnalysisResult:
    lineLength = 12
    numberOfLines = 0
    frequencyOfZero = [0] * lineLength

    # with a as input:
    for n in numbers:
        for i in range(lineLength):
            if n[i] == '0':
                frequencyOfZero[i] = frequencyOfZero[i] + 1
        numberOfLines += 1

    return AnalysisResult(lineLength, numberOfLines, frequencyOfZero)


def star1():
    with inp.read(3) as input:
        analysis = analyzeReport(input.readlines(), 12)

    majority = ceil(analysis.numberOfLines/2)

    gamma = ["0" if i >= majority else "1" for i in analysis.frequencyOfZero]
    gammaStr = "".join(gamma)

    epsilon = ["0" if i == "1" else "1" for i in gamma]
    epsilonStr = "".join(epsilon)

    print(f"""Gamma:   {gammaStr} => {int(gammaStr, 2)}""")
    print(f"""Epsilon: {epsilonStr} => {int(epsilonStr, 2)}""")
    print(f"""G*E: {int(gammaStr, 2) * int(epsilonStr, 2)}""")


def star2():
    lineLength = 12
    oxyList = []
    co2List = []

    with inp.read(3) as input:
        for line in input:
            oxyList.append(line)
            co2List.append(line)

    i = 0
    while len(oxyList) > 1 and i < lineLength:
        analysis = analyzeReport(oxyList, lineLength)
        half = (analysis.numberOfLines) / 2
        absoluteMajority = half + 1 if ceil(half) - half == 0 else ceil(half)

        # autopep8: off
        oxyMask = ["0" if i >= absoluteMajority else "1" for i in analysis.frequencyOfZero]
        # autopep8: on

        oxyList = [x for x in oxyList if x[i] == oxyMask[i]]
        i += 1

    i = 0
    while len(co2List) > 1 and i < lineLength:
        analysis = analyzeReport(co2List, lineLength)
        half = (analysis.numberOfLines) / 2
        absoluteMajority = half + 1 if ceil(half) - half == 0 else ceil(half)

        # autopep8: off
        co2Mask = ["1" if i >= absoluteMajority else "0" for i in analysis.frequencyOfZero]
        # autopep8: on

        co2List = [x for x in co2List if x[i] == co2Mask[i]]
        i += 1

    oxyRating = int(oxyList[0], 2)
    co2Rating = int(co2List[0], 2)

    # autopep8: off
    print(f"""Oxygen generator rating: {bin(oxyRating)[2:]} => {oxyRating}""")
    print(f"""CO2 scrubber rating:     {bin(co2Rating)[2:]} => {co2Rating}""")
    print(f"""Life support rating: {oxyRating * co2Rating}""")
    # autopep8: on


if __name__ == "__main__":
    star1()
    star2()
