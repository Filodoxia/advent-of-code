import input


def star1():
    clock = 0
    prgCounter = -1
    curInstrEndCycle = 0
    measurementCycles = list(range(20, 221, 40))
    nextMeasurementIndex = 0
    program = input.readLines("day10.txt")
    registerX = 1
    signalStrengthSum = 0

    while clock < measurementCycles[-1]:
        clock += 1

        # print(
        #     f"Cycle {clock}\n"
        #     f"X={registerX}, instr={program[prgCounter]} curInstrEndCycle={curInstrEndCycle}"
        # )

        if measurementCycles[nextMeasurementIndex] == clock:
            signalStrengthSum += clock*registerX
            nextMeasurementIndex += 1

        # read new instruction
        if curInstrEndCycle < clock:
            prgCounter += 1
            if program[prgCounter] == "noop":
                curInstrEndCycle = clock
            else:
                curInstrEndCycle = clock+1
        elif curInstrEndCycle == clock:
            if program[prgCounter] != "noop":
                # print(program[prgCounter])
                registerX += int(program[prgCounter].split()[1])
        else:
            raise Exception("You f***ed up")

    return signalStrengthSum


def star2():
    clock = 0
    prgCounter = -1
    curInstrEndCycle = 0
    measurementCycles = list(range(40, 241, 40))
    nextMeasurementIndex = 0
    program = input.readLines("day10.txt")
    registerX = 1
    screen = []
    currentScreenRow = []

    while clock < measurementCycles[-1]:
        clock += 1

        currentScreenRow.append(
            "█" if abs(registerX-len(currentScreenRow)) < 2 else " ")

        if measurementCycles[nextMeasurementIndex] == clock:
            screen.append(currentScreenRow)
            currentScreenRow = []
            nextMeasurementIndex += 1

        # read new instruction
        if curInstrEndCycle < clock:
            prgCounter += 1
            if program[prgCounter] == "noop":
                curInstrEndCycle = clock
            else:
                curInstrEndCycle = clock+1
        elif curInstrEndCycle == clock:
            if program[prgCounter] != "noop":
                registerX += int(program[prgCounter].split()[1])
        else:
            raise Exception("You f***ed up")

    return "\n".join("".join(row) for row in screen)


if __name__ == "__main__":
    print(star1())
    print(star2())
