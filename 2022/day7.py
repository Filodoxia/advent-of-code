from dataclasses import dataclass
import input
import math


@dataclass(kw_only=True)
class File():
    name: str
    size: int = 0


class Directory():
    # def __init__(self, name: str, parent: Union["Directory", None]) -> None:
    def __init__(self, name: str, parent: "Directory") -> None:
        self.name: str = name
        self.parent: Directory = parent
        self.dirs: dict[str, Directory] = {}
        self.files: dict[str, File] = {}

    def size(self) -> int:
        sizeOfOwnFiles = sum(map(lambda f: f.size, self.files.values()))
        sizeOfSubdirs = sum(map(lambda d: d.size(), self.dirs.values()))
        return sizeOfOwnFiles + sizeOfSubdirs


class RootDirectory(Directory):
    def __init__(self) -> None:
        super().__init__("/", self)


def star1():
    root = buildFs()
    return sumSizes(root, 100000)


def star2():
    root = buildFs()

    diskSpace = 70000000
    requiredSpace = 30000000
    # assume we need extra space
    requiredSize = abs(diskSpace - requiredSpace - root.size())

    return helper(root, requiredSize)


def buildFs() -> Directory:
    root = RootDirectory()
    root.parent = root
    wd = root

    for line in input.readLines("day7.txt"):
        tokens = line.split()

        # command
        if tokens[0] == "$":
            if tokens[1] == "cd":
                if tokens[2] == "..":
                    wd = wd.parent
                elif tokens[2] == "/":
                    wd = root
                else:
                    wd = wd.dirs[tokens[2]]

        else:
            # output
            if tokens[0] == "dir":
                # create subdir if not exist
                if not tokens[1] in wd.dirs:
                    newDir = Directory(name=tokens[1], parent=wd)
                    wd.dirs.update({tokens[1]: newDir})
            else:
                # create file
                if not tokens[1] in wd.files:
                    newFile = File(name=tokens[1], size=int(tokens[0]))
                    wd.files.update({tokens[1]: newFile})
    return root


def sumSizes(dir: Directory, maxSize: int):
    sizeSum = 0

    # add own size?
    if dir.size() <= maxSize:
        sizeSum += dir.size()

    # sum subdir sizes
    for subdir in dir.dirs.values():
        sizeSum += sumSizes(subdir, maxSize)

    return sizeSum


def helper(dir: Directory, requiredSize: int, minSize=math.inf) -> float:
    mySize = dir.size()

    # cases in which this directory and all subdirectories can be skipped
    # this directory isn't large enough
    if mySize < requiredSize:
        return minSize
    # this directory is larger than the best option found so far
    if mySize >= minSize:
        return minSize

    dirOptions = []
    dirOptions.append(mySize)

    for subdir in dir.dirs.values():
        dirOptions.append(helper(subdir, requiredSize, mySize))

    return min(dirOptions)


if __name__ == "__main__":
    print(star1())
    print(star2())
