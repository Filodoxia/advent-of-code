from os.path import abspath, dirname, join
from math import floor


def calculateFuel(mass):
    requiredFuel = floor(int(mass) / 3) - 2
    return max(0, requiredFuel)


inputFilePath = join(dirname(abspath(__file__)), 'input.txt')
with open(inputFilePath, 'r') as f:
    modules = f.read().split()

totalFuel = 0

#calculate fuel needed for all modules
for moduleMass in modules:
    fuelForModule = calculateFuel(moduleMass)
    
    #calculate additional fuel needed for the fuel itself
    additionalFuel = calculateFuel(fuelForModule)
    while additionalFuel > 0:
        fuelForModule += additionalFuel
        additionalFuel = calculateFuel(additionalFuel)

    #add total fuel requirement for that module to the overall total fuel requirement
    totalFuel += fuelForModule


print(totalFuel)