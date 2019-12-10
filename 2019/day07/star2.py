from itertools import permutations
from Amplifier import Amplifier, AmpState
from os.path import abspath, dirname, join


inputFilePath = join(dirname(abspath(__file__)), 'input.txt')
with open(inputFilePath, 'r') as f:
    intcode = [int(i) for i in f.read().split(',')]


results = []
combinations = permutations(range(5, 10), 5)

for comb in combinations:
    #init amps
    ampA = Amplifier(intcode, comb[0])
    ampB = Amplifier(intcode, comb[1])
    ampC = Amplifier(intcode, comb[2])
    ampD = Amplifier(intcode, comb[3])
    ampE = Amplifier(intcode, comb[4])

    #connect amps
    ampA.connect(ampB)
    ampB.connect(ampC)
    ampC.connect(ampD)
    ampD.connect(ampE)
    ampE.connect(ampA)

    #pass 0 as input to first amp. this starts the code execution and 
    #subsequently activates all connected amps as well and only stops
    #once all amps have halted (either in finished state or waiting for input)
    ampA.receive(0)

    #read result from 
    results.append((comb, ampE.output))

#filter results for the 
max = results[0]
for r in results:
    if r[1] > max[1]:
        max = r
print(max)