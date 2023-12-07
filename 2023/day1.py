from pathlib import Path
import re

DAY = 1
IN_FILE = Path(__file__).joinpath(f"../in/day{DAY}").resolve()


def star1():
    x = [[c for c in line if c.isdigit()]
         for line in IN_FILE.open().readlines()]
    print(sum([int(n[0] + n[-1]) for n in x]))


def star2():
    regex = re.compile(r"\d|one|two|three|four|five|six|seven|eight|nine|zero")
    regex_reverse = re.compile(
        r"\d|" + "one|two|three|four|five|six|seven|eight|nine|zero"[::-1])
    m = {
        '1': 1,
        "one": 1,
        "eno": 1,
        '2': 2,
        "two": 2,
        "owt": 2,
        '3': 3,
        "three": 3,
        "eerht": 3,
        '4': 4,
        "four": 4,
        "ruof": 4,
        '5': 5,
        "five": 5,
        "evif": 5,
        '6': 6,
        "six": 6,
        "xis": 6,
        '7': 7,
        "seven": 7,
        "neves": 7,
        '8': 8,
        "eight": 8,
        "thgie": 8,
        '9': 9,
        "nine": 9,
        "enin": 9,
        '0': 0,
        "zero": 0,
        "orez": 0,
    }
    sum = 0

    for l in IN_FILE.open().readlines():
        sum += m[regex.search(l)[0]] * 10
        sum += m[regex_reverse.search(l[::-1])[0]]

    print(sum)


if __name__ == "__main__":
    star1()
    star2()
