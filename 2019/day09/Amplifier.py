from enum import IntEnum


class AmpState(IntEnum):
    ACTIVE   = 0
    WAITING  = 1
    FINISHED = 2


class Memory():
    def __init__(self):
        self.memory = {}

    def get(self, index):
        if index not in self.memory: self.memory[index] = 0
        return self.memory[index]

    def set(self, index, value):
        self.memory[index] = value

    def print(self):
        for i in self.memory:
            print('{}: {}'.format(i, self.memory[i]))


class Amplifier():
    def __init__(self, intcode):
        self.memory = Memory()
        for i in range(len(intcode)):
            self.memory.set(i, intcode[i])
        self.ip = 0
        self.rb = 0
        self.input = []
        self.connections = []
        self.state = AmpState.WAITING


    def connect(self, amp):
        self.connections.append(amp)


    def notify(self, value):
        if len(self.connections) == 0:
            print(value)
        else:
            for con in self.connections:
                con.receive(value)


    def receive(self, value):
        self.input.insert(0, value)
        if self.state == AmpState.WAITING:
            self.state = AmpState.ACTIVE
            self.run()


    def parseInstruction(self):
        instr = self.memory.get(self.ip)
        opcode = instr % 100
        
        params = []
        instr = int(instr / 10)
        for i in range(1, 4):
            instr = int(instr / 10)
            mode = instr % 10
            if mode == 0:
                params.append(self.memory.get(self.ip + i))
            elif mode == 1:
                params.append(self.ip + i)
            elif mode == 2:
                params.append(self.memory.get(self.ip + i) + self.rb)

        return [opcode, params]


    def run(self):
        self.state = AmpState.ACTIVE
        while self.state == AmpState.ACTIVE:
            opcode, params = self.parseInstruction()
            self.execute(opcode, params)


    def execute(self, opcode, params):
        # print(opcode, *params)
        if opcode == 1:     #add
            result = self.memory.get(params[0]) + self.memory.get(params[1])
            self.memory.set(params[2], result)
            self.ip += 4

        elif opcode == 2:   #multiply
            result = self.memory.get(params[0]) * self.memory.get(params[1])
            self.memory.set(params[2], result)
            self.ip += 4

        elif opcode == 3:   #input
            self.memory.set(params[0], self.input.pop())
            self.ip += 2

        elif opcode == 4:   #output
            self.notify(self.memory.get(params[0]))
            self.ip += 2

        elif opcode == 5:   #jump-if-true
            if self.memory.get(params[0]) == 0:
                self.ip += 3
            else:
                self.ip = self.memory.get(params[1])

        elif opcode == 6:   #jump-if-false
            if self.memory.get(params[0]) == 0:
                self.ip = self.memory.get(params[1])
            else:
                self.ip += 3

        elif opcode == 7:   #less than
            comp = self.memory.get(params[0]) < self.memory.get(params[1])
            self.memory.set(params[2], 1 if comp else 0)
            self.ip += 4

        elif opcode == 8:   #equal
            comp = self.memory.get(params[0]) == self.memory.get(params[1])
            self.memory.set(params[2], 1 if comp else 0)
            self.ip += 4

        elif opcode == 9:   #adjust relative base
            self.rb += self.memory.get(params[0])
            self.ip += 2

        elif opcode == 99:  #end program
            self.state = AmpState.FINISHED