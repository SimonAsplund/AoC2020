#!/usr/bin/python3

# Open a file
from pexpect import runu
import copy

todaysInput = open("input11.txt", "r")
#todaysInput = open("testInput.txt", "r")
print("Name of the file: ", todaysInput.name)

lines = todaysInput.readlines()

for line in lines:

    line

# inputs = copy.deepcopy(inputs[25:])
#print("inputs: ", inputs)

# Close opened file
todaysInput.close()