from os.path import abspath, dirname, join
from Image import Image
inputFilePath = join(dirname(abspath(__file__)), 'input.txt')


def count(value, list:list):
    count = 0
    for v in list:
        if v == value: count += 1
    return count

with open(inputFilePath, 'r') as f:
    img = Image(f.read().split()[0], 25, 6)

layers = img.layers()
zeroesInLayers = []
for layer in layers:
    zeroesInLayers.append(count(0, layer))

layerWithLeastZeroes = zeroesInLayers.index(min(zeroesInLayers))
print(layers[layerWithLeastZeroes])
print(count(1, layers[layerWithLeastZeroes]) * count(2, layers[layerWithLeastZeroes]))