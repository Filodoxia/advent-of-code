from math import floor

with open('input.txt', 'r') as f:
    data = f.read().split()

totalFuel = 0
for mass in data:
    totalFuel += floor(int(mass) / 3) - 2

print(totalFuel)