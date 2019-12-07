INPUT_START = 156218
INPUT_END = 652527

def hasTwoIdenticalAdjacent(numberAsString):
    if len(numberAsString) == 2:
        if numberAsString[0] == numberAsString[1]:
            return True
    elif len(numberAsString) > 2:
        #if three or more digits test the first and last three for xxy or xyy, respectively
        if numberAsString[0] == numberAsString[1] and numberAsString[1] != numberAsString[2]:
            return True
        elif numberAsString[-2] == numberAsString[-1] and numberAsString[-2] != numberAsString[-3]:
            return True

        #if there are at least four digits test for pattern xyyz with y != x and y != z
        if len(numberAsString) > 3:
            for i in range(1, len(numberAsString) - 2):
                if numberAsString[i] == numberAsString[i + 1]:
                    #make sure the digits to the left and to the right of the two identical ones are different ones
                    if numberAsString[i] != numberAsString[i - 1] and numberAsString[i] != numberAsString[i + 2]:
                        return True

    #default to false if pattern wasnt matched or its is just an one digit number
    return False

def hasNoDecrease(numberAsString):
    for i in range(len(numberAsString) - 1):
        if numberAsString[i] > numberAsString[i + 1]:
            return False
    return True

def checkRules(number):
    number = str(number)
    return len(number) == 6 and hasTwoIdenticalAdjacent(number) and hasNoDecrease(number)

solutions = []
for i in range(INPUT_START, INPUT_END + 1):
    if checkRules(i):
        solutions.append(i)

print(len(solutions))