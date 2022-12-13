from os import path


def _getFilePath(filename: str):
    file_path = path.join(path.abspath(path.curdir), "input", filename)
    if not path.isfile(file_path):
        raise Exception("Input file not found")
    return file_path


def read(filename: str):
    file_content = ""

    with open(_getFilePath(filename), "r") as f:
        file_content = f.read()

    return file_content


def readLines(filename: str):
    file_content: list[str] = []

    with open(_getFilePath(filename), "r") as f:
        file_content = list(map(lambda x: x.strip(), f.readlines()))

    return file_content


def readGrid(filename: str, inLineSep: str | None = None, asInt: bool = False):
    file_content: list[list[str]] | list[list[int]] = []

    with open(_getFilePath(filename), "r") as f:
        if inLineSep:
            if asInt:
#autopep8: off
                file_content = list(map(
                    lambda x: [int(y) for y in x.strip().split(inLineSep)]
                    , f.readlines()
                ))
            else:
                file_content = [x.strip().split(inLineSep) for x in f.readlines()]
        else:
            if asInt:
                file_content = list(map(
                    lambda x: [int(y) for y in x.strip()]
                    , f.readlines()
                ))
            else:
                file_content = [[y for y in x.strip()] for x in f.readlines()]
#autopep8: on

    return file_content
