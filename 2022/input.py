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
