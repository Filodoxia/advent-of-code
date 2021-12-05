import input as inp


def star1():
    with inp.read(1) as input:
        increases = 0
        currentHeight = int(input.readline())

        for line in input:
            nextHeight = int(line)
            if nextHeight > currentHeight:
                increases += 1
            currentHeight = nextHeight

    print(f"""Increases in height: {increases}""")


def star2():
    windowLength = 3
    increases = 0

    with inp.read(1) as input:
        heights = input.readlines()

    for i in range(len(heights) - windowLength):
        if int(heights[i + windowLength]) > int(heights[i]):
            increases += 1

    print(f"""Increases in height (sliding window): {increases}""")


if __name__ == "__main__":
    star1()
    star2()
