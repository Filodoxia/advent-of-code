from os import path


def read(day: int):
    return open(path.join(path.dirname(__file__), "input", f"day{day}"), "r")
