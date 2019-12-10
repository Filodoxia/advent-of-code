from os.path import abspath, dirname, join
inputFilePath = join(dirname(abspath(__file__)), 'input.txt')


class Amplifier:
    def __init__(self, intcode, phaseSetting=0):
        self.instructionPointer = -1
        self.inputPointer = -1
        self.phaseSetting = phaseSetting
        self.intcode = intcode
        self.memory = []
        self.input = None
        self.output = None


    def setPhase(self, phaseSetting):
        self.phaseSetting = phaseSetting


    def run(self, input, debug = False):
        self.memory = [i for i in self.intcode]
        self.instructionPointer = 0
        self.input = [self.phaseSetting, input]
        self.inputPointer = 0
        self.output = None
        running = True

        while running:
            try:
                if self.executeCommand(debug) == 99: running = False
            except BaseException as err:
                running = False
                raise err

        return self.output


    def executeCommand(self, debug=False):
        # read opcode and set registers
        instruction = self.memory[self.instructionPointer]
        opcode = instruction % 100
        param1mode = int(instruction % 1000 / 100)
        param2mode = int(instruction % 10000 / 1000)

        if debug: print(instruction, opcode, param1mode, param2mode)

        if opcode == 1:
            param1 = self.memory[self.instructionPointer + 1] if param1mode == 1 else self.memory[self.memory[self.instructionPointer + 1]]
            param2 = self.memory[self.instructionPointer + 2] if param2mode == 1 else self.memory[self.memory[self.instructionPointer + 2]]
            param3 = self.memory[self.instructionPointer + 3]
            self.memory[param3] = param1 + param2
            self.instructionPointer += 4
            
        elif opcode == 2:
            param1 = self.memory[self.instructionPointer + 1] if param1mode == 1 else self.memory[self.memory[self.instructionPointer + 1]]
            param2 = self.memory[self.instructionPointer + 2] if param2mode == 1 else self.memory[self.memory[self.instructionPointer + 2]]
            param3 = self.memory[self.instructionPointer + 3]
            self.memory[param3] = param1 * param2
            self.instructionPointer += 4

        elif opcode == 3:
            param1 = self.memory[self.instructionPointer + 1]
            self.memory[param1] = self.input[self.inputPointer]
            self.inputPointer += 1
            self.instructionPointer += 2

        elif opcode == 4:
            param1 = self.memory[self.instructionPointer + 1] if param1mode == 1 else self.memory[self.memory[self.instructionPointer + 1]]
            self.output = param1
            self.instructionPointer += 2

        elif opcode == 5:   #jump-if-true
            param1 = self.memory[self.instructionPointer + 1] if param1mode == 1 else self.memory[self.memory[self.instructionPointer + 1]]
            param2 = self.memory[self.instructionPointer + 2] if param2mode == 1 else self.memory[self.memory[self.instructionPointer + 2]]
            if param1 != 0:
                self.instructionPointer = param2
            else:
                self.instructionPointer += 3

        elif opcode == 6:   #jump-if-false
            param1 = self.memory[self.instructionPointer + 1] if param1mode == 1 else self.memory[self.memory[self.instructionPointer + 1]]
            param2 = self.memory[self.instructionPointer + 2] if param2mode == 1 else self.memory[self.memory[self.instructionPointer + 2]]
            if param1 == 0:
                self.instructionPointer = param2
            else:
                self.instructionPointer += 3

        elif opcode == 7:   #less than
            param1 = self.memory[self.instructionPointer + 1] if param1mode == 1 else self.memory[self.memory[self.instructionPointer + 1]]
            param2 = self.memory[self.instructionPointer + 2] if param2mode == 1 else self.memory[self.memory[self.instructionPointer + 2]]
            param3 = self.memory[self.instructionPointer + 3]
            if param1 < param2: self.memory[param3] = 1
            else: self.memory[param3] = 0
            self.instructionPointer += 4

        elif opcode == 8:   #equals
            param1 = self.memory[self.instructionPointer + 1] if param1mode == 1 else self.memory[self.memory[self.instructionPointer + 1]]
            param2 = self.memory[self.instructionPointer + 2] if param2mode == 1 else self.memory[self.memory[self.instructionPointer + 2]]
            param3 = self.memory[self.instructionPointer + 3]
            if param1 == param2: self.memory[param3] = 1
            else: self.memory[param3] = 0
            self.instructionPointer += 4

        elif opcode == 99:
            return 99

        else:
            raise Exception('Unknown opcode {}'.format(opcode))



with open(inputFilePath, 'r') as f:
    intcode = [int(i) for i in f.read().split(',')]

combinations = []
for a in range(5):
    currentCombinationA = [a]
    for b in range(5):
        if b not in currentCombinationA:
            currentCombinationB = [*currentCombinationA, b]
            for c in range(5):
                if c not in currentCombinationB:
                    currentCombinationC = [*currentCombinationB, c]
                    for d in range(5):
                        if d not in currentCombinationC:
                            currentCombinationD = [*currentCombinationC, d]
                            for e in range(5):
                                if e not in currentCombinationD:
                                    combinations.append([*currentCombinationD, e])

ampA = Amplifier(intcode)
ampB = Amplifier(intcode)
ampC = Amplifier(intcode)
ampD = Amplifier(intcode)
ampE = Amplifier(intcode)

results = []
for comb in combinations:
    ampA.setPhase(comb[0])
    ampB.setPhase(comb[1])
    ampC.setPhase(comb[2])
    ampD.setPhase(comb[3])
    ampE.setPhase(comb[4])

    out = ampA.run(0)
    out = ampB.run(out)
    out = ampC.run(out)
    out = ampD.run(out)
    results.append((comb, ampE.run(out)))

max = results[0]
for r in results:
    if r[1] > max[1]:
        max = r

print(max)