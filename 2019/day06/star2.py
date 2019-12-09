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


def createUniverse(so, knownObjects, ooi):
    for oo in knownObjects[so.name]:
        orbitingObject = SpaceObject(oo, so)
        if oo in ooi:
            ooi[oo] = orbitingObject
        if oo in knownObjects:
            createUniverse(orbitingObject, knownObjects, ooi)


def commonAncestor(so1, so2):
    ca = None

    while ca is None:
        if so1 == so2:
            ca = so1
        elif so1.depth > so2.depth:
            so1 = so1.parent
        else:
            so2 = so2.parent

    return ca


###############################
# Code
###############################

with open(inputFilePath, 'r') as f:
    data = f.read().split()

knownObjects = {}
orbit = {}
ooi = {     #objects of interest
    'SAN': None,
    'YOU': None
}

for relation in data:
    o1, o2 = relation.split(')')

    if o1 in knownObjects:
        knownObjects[o1].add(o2)
    else:
        knownObjects[o1] = {o2}

#create root object (center of mass)
com = SpaceObject('COM')

#create the universe around the center of mass
createUniverse(com, knownObjects, ooi)

#find minimum number of orbital transfers for you to reach santa
#therefore, find common parent and then calculate path lengths to yours and Santa's orbits
ca = commonAncestor(ooi['YOU'], ooi['SAN'])
you_ca = ooi['YOU'].depth - ca.depth
santa_ca = ooi['SAN'].depth - ca.depth
print('The common ancestor is "{}" at depth {}'.format(ca.name, ca.depth))
print('Your distance to common ancestor: {}'.format(you_ca))
print('Santas distance to common ancestor: {}'.format(santa_ca))
print('Distance from you to Santa: {}'.format(you_ca + santa_ca))
print('Distance from yours to Santa\'s orbit: {}'.format(you_ca + santa_ca - 2))