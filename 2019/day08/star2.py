from os.path import abspath, dirname, join
from Image import Image
inputFilePath = join(dirname(abspath(__file__)), 'input.txt')


with open(inputFilePath, 'r') as f:
    img = Image(f.read().split()[0], 25, 6)


###########################
# Flatten the layers
###########################
#initialize the flattened layer with transparent pixels, i.e. with value 2
flattenedLayer = [2 for i in range(img.width * img.height)]

#reverse since the last layer is the bottom most
layers = img.layers()
layers.reverse()

for layer in layers:
    layerIndex = 0
    for v in layer:
        if not v == 2:
            flattenedLayer[layerIndex] = v
        layerIndex += 1

#create the output by iterating over the lines in the flattened layer
layerIndex = 0
for r in range(img.height):
    line = ''
    for c in range(img.width):
        line += '\u2588' if flattenedLayer[layerIndex] == 1 else ' '
        layerIndex += 1
    print(line)