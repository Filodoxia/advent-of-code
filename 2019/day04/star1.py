INPUT_START = 156218
INPUT_END = 652527

def hasSameAdjacent(numberAsString):
    for i in range(len(numberAsString) - 1):
        if numberAsString[i] == numberAsString[i + 1]:
            return True
    return False

def hasNoDecrease(numberAsString):
    for i in range(len(numberAsString) - 1):
        if numberAsString[i] > numberAsString[i + 1]:
            return False
    return True

def checkRules(number):
    number = str(number)
    return len(number) == 6 and hasSameAdjacent(number) and hasNoDecrease(number)

solutions = []
for i in range(INPUT_START, INPUT_END + 1):
    if checkRules(i):
        solutions.append(i)

print(len(solutions))