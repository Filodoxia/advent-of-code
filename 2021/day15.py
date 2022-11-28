from typing import List, Tuple
import input as inp
from math import inf


MIN_RISK_LEVEL = 1
MAX_RISK_LEVEL = 9
ROWS: int
COLUMNS: int
RISK_MAP: List[List[int]]


def star1():
    dijkstra((0, 0), (ROWS-1, COLUMNS-1))


def star2():
    pass


def dijkstra(STARTING_NODE: Tuple[int, int], TARGET_NODE: Tuple[int, int]):
    # distances to any position on the map and whether it has been visited
    dist = [[[inf, False] for _ in range(COLUMNS)] for _ in range(ROWS)]

    # init by considering the starting node as visited and assign its distance, i.e. its risk level
    r, c = STARTING_NODE
    dist[r][c] = [RISK_MAP[r][c], True]

    print(dist)
    # queue with unvisited nodes that are reachable from already
    # visited nodes.init with the starting node
    queue = [STARTING_NODE]

    for _ in range((ROWS*COLUMNS) - 1):
        pass

    return dist[TARGET_NODE[0]][TARGET_NODE[1]]


def parse():
    global RISK_MAP, ROWS, COLUMNS
    RISK_MAP = []

    for line in inp.read("15_test"):
        row = []
        for i in line:
            if i == "\n":
                continue

            row.append(int(i))
        RISK_MAP.append(row)

    COLUMNS = len(RISK_MAP[0])
    ROWS = len(RISK_MAP)


if __name__ == "__main__":
    parse()
    print(RISK_MAP)
    print(ROWS, COLUMNS)
    star1()
    star2()
