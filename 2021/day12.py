import input as inp


def star1(log: bool = False):
    paths = []
    q = [["start"]]

    while len(q) > 0:
        path = q.pop()

        if log:
            print("------------------------")
            print(f"""Queue: {q}""")
            print(f"""Continuing path: {path}""")

        # consider all potential neighbors
        for neighbor in AM[path[-1]]:
            if log:
                print(f"""Neighbor: {neighbor}""")

            # discard the neighbor if it's the starting cave,
            # because that may only be visited once
            if neighbor == "start":
                if log:
                    print("Start node can only be visited once.")
                continue

            # discard the neighbor also if:
            # - any cave has been visited the max amount possible,
            # - it actually is a small cave
            # - it was already visited
            if path[0] and neighbor in CAVES_SMALL and neighbor in path:
                if log:
                    print("Small cave already visited.")
                continue

            # we have a valid cave we can travel to, so add it to the path
            pathWithNextCave = path.copy()
            pathWithNextCave.append(neighbor)

            # if neighbor is the end, add the path to the path list
            # else add it back to the queue to continue it later
            if neighbor == "end":
                paths.append(pathWithNextCave)
            else:
                q.append(pathWithNextCave)

    if log:
        print("------------------------")
    print(f"""Found {len(paths)} paths through the cavern.""")


def star2(log: bool = False):
    paths = []
    q = [[False, "start"]]

    while len(q) > 0:
        path = q.pop()

        if log:
            print("------------------------")
            print(f"""Queue: {q}""")
            print(f"""Continuing path: {path}""")

        # consider all potential neighbors
        for neighbor in AM[path[-1]]:
            if log:
                print(f"""Neighbor: {neighbor}""")

            # discard the neighbor if it's the starting cave,
            # because that may only be visited once
            if neighbor == "start":
                if log:
                    print("Start node can only be visited once.")
                continue

            # discard the neighbor also if:
            # - any cave has been visited the max amount possible,
            # - it actually is a small cave
            # - it was already visited max amount possible or would
            #   be the second one to be visited the max amount
            timesVisited = path.count(neighbor)
            isSmallCave = neighbor in CAVES_SMALL
            if path[0] and isSmallCave:
                if timesVisited == 1:
                    if log:
                        print("Another cave already visited max amount times.")
                    continue
                elif timesVisited == 2:
                    if log:
                        print("Neighbor already visited  max amount times.")
                    continue

            # we have a valid cave we can travel to, so add it to the path
            pathWithNextCave = path.copy()
            pathWithNextCave.append(neighbor)
            timesVisited += 1

            if isSmallCave and timesVisited == 2:
                pathWithNextCave[0] = True

            # if neighbor is the end, add the path to the path list
            # else add it back to the queue to continue it later
            if neighbor == "end":
                paths.append(pathWithNextCave)
            else:
                q.append(pathWithNextCave)

    if log:
        print("------------------------")
    print(f"""Found {len(paths)} paths through the cavern.""")


def createAdjacencyMatrix(day: int):
    # adjacency "matrix", and list of small and big caves, respectively
    global AM, CAVES_SMALL, CAVES_BIG

    AM = {}
    CAVES_BIG = set()
    CAVES_SMALL = set()

    for edge in inp.read(day):
        nodes = edge.strip().split("-")
        nodeFrom = nodes[0]
        nodeTo = nodes[1]

        if nodeFrom == nodeFrom.lower():
            CAVES_SMALL.add(nodeFrom)
        else:
            CAVES_BIG.add(nodeFrom)

        if nodeTo == nodeTo.lower():
            CAVES_SMALL.add(nodeTo)
        else:
            CAVES_BIG.add(nodeTo)

        # if a node is new add it to the am
        if nodeFrom not in AM.keys():
            AM.update({nodeFrom: set()})
        if nodeTo not in AM.keys():
            AM.update({nodeTo: set()})

        AM[nodeFrom].add(nodeTo)
        AM[nodeTo].add(nodeFrom)


if __name__ == "__main__":
    createAdjacencyMatrix(12)
    star1()
    star2()
