from os.path import abspath, dirname, join
from Amplifier import Amplifier


inputFilePath = join(dirname(abspath(__file__)), 'input.txt')
with open(inputFilePath, 'r') as f:
    intcode = [int(i) for i in f.read().split(',')]

#solution for star1
amp = Amplifier(intcode)
amp.receive(1)
amp.run()

#solution for star2
amp = Amplifier(intcode)
amp.receive(2)
amp.run()