import input
import re


def getInitialStacks():
    """fuck parsing that input for now"""
    return [
        ["G", "F", "V", "H", "P", "S"],
        ["G", "J", "F", "B", "V", "D", "Z", "M"],
        ["G", "M", "L", "J", "N"],
        ["N", "G", "Z", "V", "D", "W", "P"],
        ["V", "R", "C", "B"],
        ["V", "R", "S", "M", "P", "W", "L", "Z"],
        ["T", "H", "P"],
        ["Q", "R", "S", "N", "C", "H", "Z", "V"],
        ["F", "L", "G", "P", "V", "Q", "J"],
    ]


REGEX_CMD = re.compile("move (\d*) from (\d*) to (\d*)")


def star1():
    inp = input.readLines("day5.txt")
    stacks = getInitialStacks()

    for cmd in inp[10:]:
        m = REGEX_CMD.match(cmd)
        cmdAmount = m.group(1)
        cmdFrom = m.group(2)
        cmdTo = m.group(3)

        for _ in range(int(cmdAmount)):
            stacks[int(cmdTo)-1].append(stacks[int(cmdFrom)-1].pop())

    top = ""
    for stack in stacks:
        top += stack.pop()

    return top


def star2():
    inp = input.readLines("day5.txt")
    stacks = getInitialStacks()

    for cmd in inp[10:]:
        m = REGEX_CMD.match(cmd)
        cmdAmount = m.group(1)
        cmdFrom = m.group(2)
        cmdTo = m.group(3)

        # move items in order
        stacks[int(cmdTo)-1].extend(stacks[int(cmdFrom)-1][-int(cmdAmount):])

        # because we are not pop()ing the items we have to explicitly remove the moved items
        stacks[int(cmdFrom)-1] = stacks[int(cmdFrom)-1][:-int(cmdAmount)]

    top = ""
    for stack in stacks:
        top += stack.pop()

    return top


if __name__ == "__main__":
    print(star1())
    print(star2())
