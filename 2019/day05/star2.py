from os.path import abspath, dirname, join
inputFilePath = join(dirname(abspath(__file__)), 'input.txt')

MEM = []
INSTRUCTION_POINTER = -1
INPUT = None
OUTPUT = None


#execute a command
def executeCommand(debug=False):
    global MEM, INSTRUCTION_POINTER, INPUT, OUTPUT

    # read opcode and set registers
    instruction = MEM[INSTRUCTION_POINTER]
    opcode = instruction % 100
    param1mode = int(instruction % 1000 / 100)
    param2mode = int(instruction % 10000 / 1000)

    if debug: print(instruction, opcode, param1mode, param2mode)

    if opcode == 1:
        param1 = MEM[INSTRUCTION_POINTER + 1] if param1mode == 1 else MEM[MEM[INSTRUCTION_POINTER + 1]]
        param2 = MEM[INSTRUCTION_POINTER + 2] if param2mode == 1 else MEM[MEM[INSTRUCTION_POINTER + 2]]
        param3 = MEM[INSTRUCTION_POINTER + 3]
        MEM[param3] = param1 + param2
        INSTRUCTION_POINTER += 4
        
    elif opcode == 2:
        param1 = MEM[INSTRUCTION_POINTER + 1] if param1mode == 1 else MEM[MEM[INSTRUCTION_POINTER + 1]]
        param2 = MEM[INSTRUCTION_POINTER + 2] if param2mode == 1 else MEM[MEM[INSTRUCTION_POINTER + 2]]
        param3 = MEM[INSTRUCTION_POINTER + 3]
        MEM[param3] = param1 * param2
        INSTRUCTION_POINTER += 4

    elif opcode == 3:
        param1 = MEM[INSTRUCTION_POINTER + 1]
        MEM[param1] = INPUT
        INSTRUCTION_POINTER += 2

    elif opcode == 4:
        param1 = MEM[INSTRUCTION_POINTER + 1] if param1mode == 1 else MEM[MEM[INSTRUCTION_POINTER + 1]]
        OUTPUT = param1
        INSTRUCTION_POINTER += 2

    elif opcode == 5:   #jump-if-true
        param1 = MEM[INSTRUCTION_POINTER + 1] if param1mode == 1 else MEM[MEM[INSTRUCTION_POINTER + 1]]
        param2 = MEM[INSTRUCTION_POINTER + 2] if param2mode == 1 else MEM[MEM[INSTRUCTION_POINTER + 2]]
        if param1 != 0:
            INSTRUCTION_POINTER = param2
        else:
            INSTRUCTION_POINTER += 3

    elif opcode == 6:   #jump-if-false
        param1 = MEM[INSTRUCTION_POINTER + 1] if param1mode == 1 else MEM[MEM[INSTRUCTION_POINTER + 1]]
        param2 = MEM[INSTRUCTION_POINTER + 2] if param2mode == 1 else MEM[MEM[INSTRUCTION_POINTER + 2]]
        if param1 == 0:
            INSTRUCTION_POINTER = param2
        else:
            INSTRUCTION_POINTER += 3

    elif opcode == 7:   #less than
        param1 = MEM[INSTRUCTION_POINTER + 1] if param1mode == 1 else MEM[MEM[INSTRUCTION_POINTER + 1]]
        param2 = MEM[INSTRUCTION_POINTER + 2] if param2mode == 1 else MEM[MEM[INSTRUCTION_POINTER + 2]]
        param3 = MEM[INSTRUCTION_POINTER + 3]
        if param1 < param2: MEM[param3] = 1
        else: MEM[param3] = 0
        INSTRUCTION_POINTER += 4

    elif opcode == 8:   #equals
        param1 = MEM[INSTRUCTION_POINTER + 1] if param1mode == 1 else MEM[MEM[INSTRUCTION_POINTER + 1]]
        param2 = MEM[INSTRUCTION_POINTER + 2] if param2mode == 1 else MEM[MEM[INSTRUCTION_POINTER + 2]]
        param3 = MEM[INSTRUCTION_POINTER + 3]
        if param1 == param2: MEM[param3] = 1
        else: MEM[param3] = 0
        INSTRUCTION_POINTER += 4

    elif opcode == 99:
        return 99

    else:
        raise Exception('Unknown opcode {}'.format(opcode))


#method that runs an intcode program provided as list
def run(intcode, debug=False):
    global MEM, INSTRUCTION_POINTER, INPUT, OUTPUT

    MEM = [i for i in intcode]
    INSTRUCTION_POINTER = 0
    INPUT = 5
    OUTPUT = None
    running = True

    while running:
        try:
            if executeCommand(debug) == 99: running = False
        except BaseException as err:
            running = False
            raise err
    
    print(OUTPUT)


with open(inputFilePath, 'r') as f:
    intcode = [int(i) for i in f.read().split(',')]
    run(intcode)