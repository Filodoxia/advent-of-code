import input

DAY = 00
TEST1 = True
TEST2 = True
DEBUG1 = True
DEBUG2 = True


def getInput(part: int):
    filename = f"""day{DAY}{"_test" if (TEST1 if part==1 else TEST2) else ""}.txt"""
    return input.read(filename)


def star1():
    getInput(1)
    return "Star 1"


def star2():
    getInput(2)
    return "Star 2"


if __name__ == "__main__":
    print(star1())
    print(star2())
