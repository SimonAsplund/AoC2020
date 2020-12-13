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

def turnRight(WNpos, WEpos):
    tempN = WNpos
    WNpos = -1 * WEpos
    WEpos = tempN

    return WNpos, WEpos

def turnLeft(currentDir):
    if currentDir == "E":
        return "N"
    elif currentDir == "N":
        return "W"
    elif currentDir == "W":
        return "S"
    elif currentDir == "S":
        return "E"

def turnLeft(WNpos, WEpos):
    tempN = WNpos
    WNpos = WEpos
    WEpos = -1 * tempN

    return WNpos, WEpos


def newDir(currentDir, instruction):
    # @print("Current: ", currentDir, "   ins: ", instruction)
    if "R" in instruction:
        for i in range(0, int(int(instruction.split("R")[1]) / 90)):
            currentDir = turnRight(currentDir)
    else:
        for i in range(0, int(int(instruction.split("L")[1]) / 90)):
            currentDir = turnLeft(currentDir)

    return currentDir

def newDir(WNpos, WEpos, instruction):
    # @print("Current: ", currentDir, "   ins: ", instruction)
    if "R" in instruction:
        for i in range(0, int(int(instruction.split("R")[1]) / 90)):
            WNpos, WEpos = turnRight(WNpos, WEpos)
    else:
        for i in range(0, int(int(instruction.split("L")[1]) / 90)):
            WNpos, WEpos = turnLeft(WNpos, WEpos)

    return WNpos, WEpos
 
todaysInput = open("input12.txt", "r")
# todaysInput = open("testInput.txt", "r")
print("Name of the file: ", todaysInput.name)
lines = todaysInput.readlines()

direction = "E"
WNpos = 1
WEpos = 10

SNpos = 0
SEpos = 0

for line in lines:
    line = line.rstrip()
    print("command: ", line)

    if "R" in line or "L" in line:
        WNpos, WEpos = newDir(WNpos, WEpos, line)
        # print("New Dir: ", direction)

    elif "N" in line:
        WNpos = WNpos + int(line.split("N")[1])

    elif "S" in line:
        WNpos = WNpos - int(line.split("S")[1])

    elif "E" in line:
        WEpos = WEpos + int(line.split("E")[1])

    elif "W" in line:
        WEpos = WEpos - int(line.split("W")[1])

    elif "F" in line:
        SNpos = SNpos + WNpos * int(line.split("F")[1])
        SEpos = SEpos + WEpos * int(line.split("F")[1])

    else:
        print("ERROR!")

    print("New W Pos E: ", WEpos, " N:", WNpos)
    print("New S Pos E: ", SEpos, " N:", SNpos)

print(abs(SNpos) + abs(SEpos))
# Close opened file
todaysInput.close()
