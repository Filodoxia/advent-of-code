from typing import List, Literal
import input as inp


def star1():
    positions = inp.readIntArray(7)
    print(f"""{findBestFuelConsumption(positions,"simple")}""")


def star2():
    positions = inp.readIntArray(7)
    print(f"""{findBestFuelConsumption(positions,"complex")}""")


def findBestFuelConsumption(positions: List[int], consumptionModel: Literal["simple", "complex"]):
    model = "s" if consumptionModel == "simple" else "c"
    maxPosition = max(positions)
    bestFuelConsumption = float("inf")

    for targetPosition in range(maxPosition+1):
        fuelConsumption = 0

        for p in positions:
            if model == "s":
                fuelConsumption += abs(targetPosition - p)
            elif model == "c":
                distance = abs(targetPosition - p)
                fuelConsumption += (distance**2 + distance)/2  # (n*(n+1))/2

            if fuelConsumption > bestFuelConsumption:
                break

        if fuelConsumption < bestFuelConsumption:
            bestFuelConsumption = fuelConsumption

    return bestFuelConsumption


if __name__ == "__main__":
    star1()
    star2()
