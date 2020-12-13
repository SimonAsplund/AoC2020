#!/usr/bin/python3

# Open a file
from pexpect import runu
import copy

todaysInput = open("input13.txt", "r")
# todaysInput = open("testInput.txt", "r")
print("Name of the file: ", todaysInput.name)
lines = todaysInput.readlines()

depature = int(lines[0].rstrip())
inputs = lines[1].rstrip().split(',')
minDeltaTime = depature

saveID = 0

print(lines)
print(inputs)
print(depature)

for time in inputs:

    if time == 'x':
        continue

    print("let's test: ", time)

    startTime = int(time)
    maxDepatureTime = depature + startTime*5
    diff = 0

    while startTime <= maxDepatureTime:

        if startTime < depature:
            startTime += int(time)
            continue

        diff = abs(depature-startTime)

        if diff < minDeltaTime:
            print("ID: ", time, " wait: ", diff)
            minDeltaTime = diff
            saveID = int(time)

        startTime += int(time)

    print()

print(saveID*minDeltaTime)

# Close opened file
todaysInput.close()
