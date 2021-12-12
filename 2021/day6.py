from typing import List
import input as inp
import numpy as np


def star1():
    LAST_DAY = 80
    with inp.read(6) as input:
        fishes = list(map(int, input.readline().split(",")))

    naiveSimulate(LAST_DAY, fishes)
    # smartSimulate(LAST_DAY, fishes, 8, 6)
    print(f"""Fishes after {LAST_DAY} days: {len(fishes)}""")


def star2():
    LAST_DAY = 256
    with inp.read(6) as input:
        fishes = list(map(int, input.readline().split(",")))

    population = smartSimulate(LAST_DAY, fishes, 8, 6)

    print(f"""Fishes after {LAST_DAY} days: {sum(population)}""")


def naiveSimulate(days: int, fishes: List[int]) -> None:
    for _ in range(days):
        newFishes = 0

        for i in range(len(fishes)):
            if fishes[i] == 0:
                fishes[i] = 6
                newFishes += 1
            else:
                fishes[i] -= 1

        for i in range(newFishes):
            fishes.append(8)


def smartSimulate(days: int, fishes: List[int], dimension: int, resetTime: int) -> np.ndarray:
    population = [0]*(dimension+1)
    for f in fishes:
        population[f] += 1

    transitionMatrix = []
    for r in range(dimension+1):
        row = [0]*(dimension+1)
        row[(r+1) % (dimension+1)] = 1
        transitionMatrix.append(row)

    transitionMatrix[resetTime][0] = 1
    transitionMatrix = np.array(transitionMatrix, dtype='object')

    finalTransitionMatrix = transitionMatrix.copy()
    for _ in range(days-1):
        finalTransitionMatrix = np.matmul(
            finalTransitionMatrix, transitionMatrix)

    population = finalTransitionMatrix.dot(np.array(population))
    return population


if __name__ == "__main__":
    star1()
    star2()
