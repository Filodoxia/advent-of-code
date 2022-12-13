import input


DAY = 13
TEST1 = False
TEST2 = False
DEBUG1 = False
DEBUG2 = False


def getInput(part: int):
    i = input.read(
        f"""day{DAY}{"_test" if (TEST1 if DAY==1 else TEST2) else ""}.txt""").strip().split("\n\n")
    i = [tuple(map(eval, pair.split("\n"))) for pair in i]

    # if DEBUG:
    #     for pair in i:
    #         print(pair[0])
    #         print(pair[1])
    #         print("")

    return i


def isInOrder(pair: tuple[int | list, int | list]) -> bool:
    l = pair[0]
    r = pair[1]
    undecided = False

    if DEBUG1:
        print(pair)

    if not (type(l) == type(r)):
        if isinstance(l, int):
            l = [l]
        else:
            r = [r]

    # both are integer
    if isinstance(l, int) and isinstance(r, int):
        if l < r:
            return True
        elif l > r:
            return False
        else:
            undecided = True
    elif isinstance(l, list) and isinstance(r, list):
        shorterLength = min(len(l), len(r))
        for i in range(shorterLength):
            try:
                return isInOrder((l[i], r[i]))
            except:
                pass

        if len(l) < len(r):
            return True
        elif len(l) > len(r):
            return False
        else:
            undecided = True

    # if undecided:
    raise Exception("undecided")


def star1():
    pairs = getInput(1)
    inOrderSum = 0

    for i, pair in enumerate(pairs, 1):
        r = isInOrder(pair)

        if DEBUG1:
            print(f"Pair {i} in order: {r}")

        if r:
            inOrderSum += i

    return f"Star 1: {inOrderSum}"


def star2():
    pairs = getInput(2)
    packets = [[[2]], [[6]]]
    for pair in pairs:
        packets.append(pair[0])
        packets.append(pair[1])

    isSorted = False
    while not isSorted:
        isSorted = True
        for i in range(len(packets)-1):
            swap = not isInOrder((packets[i], packets[i+1]))
            if swap:
                p = packets[i]
                packets[i] = packets[i+1]
                packets[i+1] = p
                isSorted = False

    return "\n".join([f"{i}: {p}" for i, p in enumerate(packets, 1)])


if __name__ == "__main__":
    print(star1())
    print(star2())
    print(
        f"You have to manually look for divider packets [[2]] and [[6]] and"
        f" multiply their indices (should be 128 and 216)."
    )
