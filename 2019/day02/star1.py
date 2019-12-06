from os.path import abspath, dirname, join


#execute a command
def executeCommand(mem, opcode, in1Addr, in2Addr, outAddr):
    #errors will most likely be triggered by invalid in-/output memory addresses
    try:
        if opcode == 1:
            mem[outAddr] = mem[in1Addr] + mem[in2Addr]
        elif opcode == 2:
            mem[outAddr] = mem[in1Addr] * mem[in2Addr]
        else:
            raise Exception('Unknown opcode {}'.format(opcode))
    except BaseException as err:
        print(err)


#method that runs an intcode program provided as list
def run(mem):
    memLength = len(mem)
    running = True
    pos = 0

    while running and pos < memLength:
        opcode = mem[pos]
        in1Addr = mem[pos + 1]
        in2Addr = mem[pos + 2]
        outAddr = mem[pos + 3]

        if opcode == 99:
            running = False
        else:
            executeCommand(mem, opcode, in1Addr, in2Addr, outAddr)

        pos += 4


inputFilePath = join(dirname(abspath(__file__)), 'input.txt')
with open(inputFilePath, 'r') as f:
    mem = [int(i) for i in f.read().split(',')]

#perform the required memory cleanup
mem[1] = 12
mem[2] = 2

run(mem)
print(mem[0])