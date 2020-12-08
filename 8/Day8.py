#!/usr/bin/python3

# Open a file
from pexpect import runu

#5710 to low

todaysInput = open("input8.txt", "r")
#todaysInput = open("testInput8.txt", "r")
print("Name of the file: ", todaysInput.name)

lines = todaysInput.readlines()

commands = []

eternaty = False

for line in lines:

    commands.append(line)

place = 0

accum = 0

visited = []

#print(commands)
#print(commands[place])

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

    else:
        visited.append(place)

# Close opened file
todaysInput.close()