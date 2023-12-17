from pathlib import Path
import re

IN_FILE = Path(__file__).joinpath("../in/day2").resolve()

rx_games = re.compile(r"Game (\d*): (.*)")
rx_sample = re.compile(r"(\d*) (red|green|blue)")


def star1():
    bag = {
        "red": 12,
        "green": 13,
        "blue": 14
    }

    valid_games = []

    for game in IN_FILE.open().readlines():
        m = rx_games.match(game)
        valid = True

        for sample in m.group(2).split(";"):
            for draw in rx_sample.finditer(sample):
                if int(draw.group(1)) > bag[draw.group(2)]:
                    valid = False
                    break

        if valid:
            valid_games.append(int(m.group(1)))

    print(sum(valid_games))


def star2():
    powers = []

    for game in IN_FILE.open().readlines():
        m = rx_games.match(game)
        bag = [0, 0, 0]  # (red,green,blue)

        for sample in m.group(2).split(";"):
            for draw in rx_sample.finditer(sample):
                if draw.group(2) == "red":
                    bag[0] = max(int(draw.group(1)), bag[0])
                elif draw.group(2) == "green":
                    bag[1] = max(int(draw.group(1)), bag[1])
                elif draw.group(2) == "blue":
                    bag[2] = max(int(draw.group(1)), bag[2])

        powers.append(bag[0]*bag[1]*bag[2])

    print(sum(powers))


if __name__ == "__main__":
    star1()
    star2()
