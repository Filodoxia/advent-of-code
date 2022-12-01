from pathlib import Path


def star1():
    p = "./2022/input/day1.txt"
    input = Path(p).resolve().read_text()
    inventory = []

    currentInv = 0
    for line in input.splitlines(keepends=True):
        if line == "\n":
            inventory.append(currentInv)
            currentInv = 0
        else:
            currentInv += int(line)

    return f"{max(inventory)} calories are carried by the Elf with the most calories."


def star2():
    p = "./2022/input/day1.txt"
    input = Path(p).resolve().read_text()
    inventory = []

    currentInv = 0
    for line in input.splitlines(keepends=True):
        if line == "\n":
            inventory.append(currentInv)
            currentInv = 0
        else:
            currentInv += int(line)

    inventory.sort(reverse=True)
    return f"{sum(inventory[:3])} calories are carried by the three Elves carrying the most calories."


if __name__ == "__main__":
    print(star1())
    print(star2())
