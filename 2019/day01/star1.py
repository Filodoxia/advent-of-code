from os.path import abspath, dirname, join
from math import floor


inputFilePath = join(dirname(abspath(__file__)), 'input.txt')
with open(inputFilePath, 'r') as f:
    data = f.read().split()

totalFuel = 0
for mass in data:
    totalFuel += floor(int(mass) / 3) - 2

print(totalFuel)