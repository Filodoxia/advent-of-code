from os.path import abspath, dirname, join
inputFilePath = join(dirname(abspath(__file__)), 'input.txt')


###############################
# Definitions
###############################

class SpaceObject:
    def __init__(self, name, parent = None):
        self.name = name
        self.parent = parent
        self.orbit = []

        if parent is None:
            self.depth = 0
        else:
            self.depth = parent.depth + 1
            parent.orbit.append(self)


def createUniverse(so, knownObjects):
    for oo in knownObjects[so.name]:
        orbitingObject = SpaceObject(oo, so)
        if oo in knownObjects:
            createUniverse(orbitingObject, knownObjects)


def visitOrbit(so):
    if len(so.orbit) == 0:
        return so.depth
    else:
        orbitDepth = so.depth
        for oo in so.orbit:
            orbitDepth += visitOrbit(oo)
        return orbitDepth


###############################
# Code
###############################

with open(inputFilePath, 'r') as f:
    data = f.read().split()

knownObjects = {}
orbit = {}

for relation in data:
    o1, o2 = relation.split(')')

    if o1 in knownObjects:
        knownObjects[o1].add(o2)
    else:
        knownObjects[o1] = {o2}

#create root object (center of mass)
com = SpaceObject('COM')

#create the universe around the center of mass
createUniverse(com, knownObjects)

#print the total number of direct and indirect orbits
print(visitOrbit(com))