from os.path import abspath, dirname, join
inputFilePath = join(dirname(abspath(__file__)), 'input.txt')


def parseEdge(edge):
    direction = edge[0]
    dimension = 'x'
    distance = 0

    if direction == 'U':
        dimension = 'y'
        distance = int(edge[1:])
    elif direction == 'D':
        dimension = 'y'
        distance = -int(edge[1:])
    elif direction == 'R':
        dimension = 'x'
        distance = int(edge[1:])
    elif direction == 'L':
        dimension = 'x'
        distance = -int(edge[1:])
    
    return [dimension, distance]


with open(inputFilePath, 'r') as f:
    paths = f.read().split()

pathA = paths[0].split(',')
pathB = paths[1].split(',')


#get maximum and minimum x and y values of first path assuming we start at (0,0)
minX = 0
maxX = 0
minY = 0
maxY = 0
x = 0
y = 0
for edge in pathA:
    direction = edge[0]
    if direction == 'U':
        y += int(edge[1:])
    elif direction == 'D':
        y -= int(edge[1:])
    elif direction == 'R':
        x += int(edge[1:])
    elif direction == 'L':
        x -= int(edge[1:])

    if x > maxX:
        maxX = x

    if x < minX:
        minX = x

    if y > maxY:
        maxY = y

    if y < minY:
        minY = y


#store all coordinates the first wire passes through
#for easier lookup later on use a set for each row
print('Creating "circuit board" for first wire...')
portX = abs(minX)
portY = abs(minY)
w = portX + maxX
h = portY + maxY
mapA = [set() for y in range(h + 1)]

pathAPoints = []
x = portX
y = portY
for edge in pathA:
    dimension, distance = parseEdge(edge)

    if dimension == 'x':
        if distance >= 0:
            r = range(x + 1, x + distance + 1)
        else:
            r = range(x - 1, x + distance - 1, -1)
        
        for i in r:
            mapA[y].add(i)
            pathAPoints.append((i,y))
            
        x += distance
    else:
        if distance >= 0:
            r = range(y + 1, y + distance + 1)
        else:
            r = range(y - 1, y + distance - 1, -1)
        
        for i in r:
            mapA[i].add(x)
            pathAPoints.append((x,i))
            
        y += distance


#follow the second wire and find intersections
print('Finding intersections...')
intersections = []
pathBPoints = []
x = portX
y = portY

for edge in pathB:
    dimension, distance = parseEdge(edge)

    if dimension == 'x':
        if distance >= 0:
            r = range(x + 1, x + distance + 1)
        else:
            r = range(x - 1, x + distance - 1, -1)
        
        for i in r:
            try:
                pathBPoints.append((i,y))
                if i in mapA[y]:
                    intersections.append((i, y))
            except:
                pass

        x += distance
    else:
        if distance >= 0:
            r = range(y + 1, y + distance + 1)
        else:
            r = range(y - 1, y + distance - 1, -1)
        
        for i in r:
            pathBPoints.append((x,i))
            try:
                if x in mapA[i]:
                    intersections.append((x, i))
            except:
                pass
            
        y += distance 


#find fewest combined steps the wires must take to reach an intersection
print('Find closest intersection of wires...')
combinedSteps=[pathAPoints.index(inters) + pathBPoints.index(inters) + 2 for inters in intersections]
print('Intersections: {}'.format(intersections))
print('Combined steps: {}'.format(combinedSteps))
print('Min steps: {}'.format(min(combinedSteps)))