#!/usr/bin/python3

# Open a file
from pexpect import runu

import copy

#313 to low


def testCommands(commands):

    eternaty = False
    place = 0
    accum = 0
    visited = []
    
    while eternaty == False:
        com = commands[place]
        com = com.rstrip()

        if "acc" in com:
            if "+" in com:
                accum = accum + int(com.split("+")[1])
            else:
                accum = accum - int(com.split("-")[1])

            place = place + 1

        elif "jmp" in com:
            if "+" in com:
                place = place + int(com.split("+")[1])
            else:
                place = place - int(com.split("-")[1])

        elif "nop" in com:
            place = place + 1

        if place in visited:
            eternaty = True
            print("acc: " , accum)

        elif place >= len(commands) - 1:
            print(" True acc: " , accum)

        else:
            visited.append(place)

    visited.append(place)
    #print("visited: " , visited)



todaysInput = open("input8.txt", "r")
#todaysInput = open("testInput8.txt", "r")
print("Name of the file: ", todaysInput.name)

lines = todaysInput.readlines()

commands = []

eternaty = False

for line in lines:

    commands.append(line)

#testCommands(commands)

nops = []
jmps = []
place = 0
# find all nop and jmp


for line in lines:
    if "nop" in line:
        nops.append(place)
    elif "jmp" in line:
        jmps.append(place)
    place = place + 1

maybe = []
for change in nops:

    maybe = copy.deepcopy(commands)

    print("First: ", maybe[change])
    maybe[change] = "jmp" + maybe[change].split("nop")[1]
    print("Then:  ", maybe[change])
    testCommands(maybe)

for change in jmps:

    maybe = copy.deepcopy(commands)

    #print("First: ", maybe[change])
    maybe[change] = "nop" + maybe[change].split("jmp")[1]
    #print("Then: ", maybe[change])
    testCommands(maybe) 

# Close opened file
todaysInput.close()