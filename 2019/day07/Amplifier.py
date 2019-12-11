from enum import Enum


class AmpState(Enum):
    INITIALIZED = 0
    RUNNING     = 1
    WAITING     = 2
    FINISHED    = 3


class Amplifier:
    def __init__(self, intcode:list, phaseSetting:int):
        self.intcode = intcode
        self.memory = [i for i in intcode]
        self.ip = 0

        self.input = [phaseSetting]
        self.output = None
        self.connections = []

        self.state = AmpState.INITIALIZED


    def connect(self, amp):
        self.connections.append(amp)


    def notify(self):
        for con in self.connections:
            con.receive(self.output)


    def receive(self, input):
        self.input.append(input)
        if self.state in [AmpState.WAITING, AmpState.INITIALIZED]:
            self.run()


    def run(self):
        #run until finished or input needed
        self.state = AmpState.RUNNING
        while self.state == AmpState.RUNNING:
            self.step()


    def step(self):
        opcode, paramModes = self.processInstruction(self.memory[self.ip])
        
        if opcode == 99:
            self.state = AmpState.FINISHED
        else:
            self.executeCommand(opcode, paramModes)


    def processInstruction(self, instr) -> list:
        opcode = instr % 100
        mode1 = int(instr % 1000 / 100)
        mode2 = int(instr % 10000 / 1000)
        mode3 = int(instr % 100000 / 10000)
        return [opcode, [mode1, mode2, mode3]]


    def getParam(self, pointer, mode):
        if mode == 1:
            return self.memory[pointer]
        else:
            return self.memory[self.memory[pointer]]


    def executeCommand(self, opcode, paramModes):
        if opcode == 1:     #add
            param1 = self.getParam(self.ip + 1, paramModes[0])
            param2 = self.getParam(self.ip + 2, paramModes[1])
            self.memory[self.memory[self.ip + 3]] = param1 + param2
            self.ip += 4

        elif opcode == 2:   #multiply
            param1 = self.getParam(self.ip + 1, paramModes[0])
            param2 = self.getParam(self.ip + 2, paramModes[1])
            self.memory[self.memory[self.ip + 3]] = param1 * param2
            self.ip += 4

        elif opcode == 3:   #input
            if len(self.input) == 0:
                self.state = AmpState.WAITING
                return
            self.memory[self.memory[self.ip + 1]] = self.input.pop(0)
            self.ip += 2

        elif opcode == 4:   #output
            param = self.getParam(self.ip + 1, paramModes[0])
            self.output = param
            self.ip += 2
            self.notify()

        elif opcode == 5:   #jump-if-true
            param1 = self.getParam(self.ip + 1, paramModes[0])
            param2 = self.getParam(self.ip + 2, paramModes[1])
            if param1 != 0:
                self.ip = param2
            else:
                self.ip += 3

        elif opcode == 6:   #jump-if-false
            param1 = self.getParam(self.ip + 1, paramModes[0])
            param2 = self.getParam(self.ip + 2, paramModes[1])
            if param1 == 0:
                self.ip = param2
            else:
                self.ip += 3

        elif opcode == 7:   #less than
            param1 = self.getParam(self.ip + 1, paramModes[0])
            param2 = self.getParam(self.ip + 2, paramModes[1])
            comp = 1 if param1 < param2 else 0
            self.memory[self.memory[self.ip + 3]] = comp
            self.ip += 4

        elif opcode == 8:   #equals
            param1 = self.getParam(self.ip + 1, paramModes[0])
            param2 = self.getParam(self.ip + 2, paramModes[1])
            comp = 1 if param1 == param2 else 0
            self.memory[self.memory[self.ip + 3]] = comp
            self.ip += 4