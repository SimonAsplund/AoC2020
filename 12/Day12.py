#!/usr/bin/python3

# Open a file
from pexpect import runu
import copy


# 5315 to high
# 285 to low

def turnRight(currentDir):
    if currentDir == "E":
        return "S"
    elif currentDir == "S":
        return "W"
    elif currentDir == "W":
        return "N"
    elif currentDir == "N":
        return "E"

def turnLeft(currentDir):
    if currentDir == "E":
        return "N"
    elif currentDir == "N":
        return "W"
    elif currentDir == "W":
        return "S"
    elif currentDir == "S":
        return "E"

def newDir(currentDir, instruction):
    # @print("Current: ", currentDir, "   ins: ", instruction)
    if "R" in instruction:
        for i in range(0, int(int(instruction.split("R")[1]) / 90)):
            currentDir = turnRight(currentDir)
    else:
        for i in range(0, int(int(instruction.split("L")[1]) / 90)):
            currentDir = turnLeft(currentDir)

    return currentDir

todaysInput = open("input12.txt", "r")
# todaysInput = open("testInput.txt", "r")
print("Name of the file: ", todaysInput.name)
lines = todaysInput.readlines()

direction = "E"
Npos = 0
Epos = 0
n = 0

for line in lines:
    n += 1
    line = line.rstrip()
    print("command: ", line)

    if "R" in line or "L" in line:
        direction = newDir(direction, line)
        # print("New Dir: ", direction)

    elif "N" in line:
        Npos = Npos + int(line.split("N")[1])
    elif direction == "N" and "F" in line:
        Npos = Npos + int(line.split("F")[1])

    elif "S" in line:
        Npos = Npos - int(line.split("S")[1])
    elif direction == "S" and "F" in line:
        Npos = Npos - int(line.split("F")[1])

    elif "E" in line:
        Epos = Epos + int(line.split("E")[1])
    elif direction == "E" and "F" in line:
        Epos = Epos + int(line.split("F")[1])

    elif "W" in line:
        Epos = Epos - int(line.split("W")[1])
    elif direction == "W" and "F" in line:
        Epos = Epos - int(line.split("F")[1])
    else:
        print("ERROR!")

    print("New Pos E: ", Epos, " N:", Npos)

print(abs(Epos) + abs(Npos))
# Close opened file
todaysInput.close()
