import input

# start-of-package marker length
SOP_LENGTH = 4
# start-of-message marker length
SOM_LENGTH = 14


def star1():
    datagram = input.read("day6.txt").strip()
    return findMarker(datagram, SOP_LENGTH)


def star2():
    datagram = input.read("day6.txt").strip()
    return findMarker(datagram, SOM_LENGTH)


def findMarker(datagram: str, markerLength: int):
    if len(datagram) < markerLength:
        return -1

    # revolving window
    nextWindowPos = 0
    # initialize window with first "markerLength" chars
    window = [x for x in datagram[:markerLength]]

    for i in range(markerLength, len(datagram)):
        window[nextWindowPos] = datagram[i]

        # set only retains unique chars -> if length of list with unique chars
        # from window is "markerLength" we found the marker after i+1 chars
        if len(set(window)) == markerLength:
            return i+1

        nextWindowPos = (nextWindowPos+1) % markerLength

    return -1


if __name__ == "__main__":
    print(star1())
    print(star2())
