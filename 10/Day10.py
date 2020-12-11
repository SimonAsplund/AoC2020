#!/usr/bin/python3

# Open a file
from pexpect import runu
import copy

todaysInput = open("input10.txt", "r")
#todaysInput = open("testInput8.txt", "r")
print("Name of the file: ", todaysInput.name)

lines = todaysInput.readlines()

adapters = []

for line in lines:

    adapters.append(int(line))

adapters.sort()
# preamble = copy.deepcopy(inputs[:25])
print("adapters: ", adapters)
# inputs = copy.deepcopy(inputs[25:])
#print("inputs: ", inputs)

# Close opened file
todaysInput.close()