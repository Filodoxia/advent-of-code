from os.path import abspath, dirname, join
inputFilePath = join(dirname(abspath(__file__)), 'input.txt')


def manhattan(x1, x2, y1, y2):
    return abs(x1 - x2) + abs(y1 - y2)


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


#create a matrix as "circuit board" for the wire
print('Creating "circuit board" for first wire...')
portX = abs(minX)
portY = abs(minY)
w = portX + maxX
h = portY + maxY
mapA = [[0 for x in range(w + 1)] for y in range(h + 1)]
mapA[portY][portX] = 'P'

#assign every coordinate the first wire runs through a 1
print('Drawing first path...')
xStart = portX
xEnd   = portX
yStart = portY
yEnd   = portY
for edge in pathA:
    direction = edge[0]
    xStart = xEnd
    yStart = yEnd
    
    if direction == 'U':
        yEnd += int(edge[1:])
        xRange = range(xStart, xEnd+1)
        yRange = range(yStart, yEnd+1)
    elif direction == 'D':
        yEnd -= int(edge[1:])
        xRange = range(xStart, xEnd+1)
        yRange = range(yStart, yEnd-1, -1)
    elif direction == 'R':
        xEnd += int(edge[1:])
        xRange = range(xStart, xEnd+1)
        yRange = range(yStart, yEnd+1)
    elif direction == 'L':
        xEnd -= int(edge[1:])
        xRange = range(xStart, xEnd-1, -1)
        yRange = range(yStart, yEnd+1)

    for y in yRange:
        for x in xRange:
            mapA[y][x] = 0 if mapA[y][x] == 'P' else 1


#follow the second wire and find intersections
print('Finding intersections...')
intersections = []
xStart = abs(minX)
xEnd   = abs(minX)
yStart = abs(minY)
yEnd   = abs(minY)
for edge in pathB:
    direction = edge[0]
    xStart = xEnd
    yStart = yEnd
    
    if direction == 'U':
        yEnd += int(edge[1:])
        xRange = range(xStart, xEnd+1)
        yRange = range(yStart, yEnd+1)
    elif direction == 'D':
        yEnd -= int(edge[1:])
        xRange = range(xStart, xEnd+1)
        yRange = range(yStart, yEnd-1, -1)
    elif direction == 'R':
        xEnd += int(edge[1:])
        xRange = range(xStart, xEnd+1)
        yRange = range(yStart, yEnd+1)
    elif direction == 'L':
        xEnd -= int(edge[1:])
        xRange = range(xStart, xEnd-1, -1)
        yRange = range(yStart, yEnd+1)

    for y in yRange:
        for x in xRange:
            try:
                if mapA[y][x] == 1:
                    intersections.append((x,y))
            except:
                #just pass since the second wire may run outside the "circuit board" of the first wire, which results in an index out of range exception
                pass


#find intersection with minimum Manhattan distance to the central port (0,0)
print('Find closest intersection of wires...')
distances = [manhattan(portX, intersection[0], portY, intersection[1]) for intersection in intersections]
minDistance = min(distances)

for i in range(len(intersections)):
    print('{} units to intersection at {}'.format(distances[i], intersections[i]))

print('--------------------------------------')
print('Minimal distance is {}'.format(minDistance))
print('--------------------------------------')