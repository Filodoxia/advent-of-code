import input


def star1():
    prioSum = 0
    for backpack in input.readLines("day3.txt"):
        mid = int(len(backpack)/2)
        comp1 = backpack[mid:]
        comp2 = backpack[:mid]
        prioSum += getItemPriority(getDuplicates(comp1, comp2).pop())

    return prioSum


def star2():
    inp = input.readLines("day3.txt")
    prioSum = 0

    for n in range(0, len(inp), 3):
        backpack1 = inp[n]
        backpack2 = inp[n+1]
        backpack3 = inp[n+2]

        # simply treat the first 2 backbacks as compartments to find duplicates, then
        for d in getDuplicates(backpack1, backpack2):
            if d in backpack3:
                prioSum += getItemPriority(d)

    return prioSum


def getDuplicates(compartment1: str, compartment2: str):
    tried: set[str] = set()
    found: set[str] = set()

    for item in compartment1:
        if item not in tried:
            tried.add(item)
            if item in compartment2:
                found.add(item)

    return found


def getItemPriority(item: str):
    ascii = ord(item)
    return (ascii & 31) + (26 if ascii < 97 else 0)


if __name__ == "__main__":
    print(star1())
    print(star2())
