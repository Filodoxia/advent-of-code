import re
from pathlib import Path

DAY = int(re.search(r"day(\d+).py", __file__)[1])
IN_PATH = Path(__file__).parent.joinpath(f"in/day{DAY}").resolve()
INPUT = open(IN_PATH, mode="r").readlines()

RE_MUL = re.compile(r"mul\((\d{1,3}),(\d{1,3})\)")
RE_DO_BLOCKS = re.compile(r"(do\(\).*?don't\(\))*", flags=re.MULTILINE)


def star1():
    result = 0

    for section in INPUT:
        for match in RE_MUL.finditer(section):
            a, b = match.groups()
            result += int(a) * int(b)

    print(f"Star 1: {result}")


def star2():
    program = "do()"
    result = 0

    for section in INPUT:
        program += section.rstrip("\n")

    program += "don't()"

    for do_block in RE_DO_BLOCKS.finditer(program):
        if do_block.end() - do_block.start() == 0:
            continue

        for match in RE_MUL.finditer(do_block.group(0)):
            a, b = match.groups()
            result += int(a) * int(b)

    print(f"Star 2: {result}")


if __name__ == "__main__":
    star1()
    star2()
