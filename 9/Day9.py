#!/usr/bin/python3

# Open a file
from pexpect import runu
import copy
#3, 4, 28, 655

# 36430805599384 too high 

def getSums(inp):
    sums = [] 
    for i in range(0,len(inp)):

        for n in range(0,len(inp)):
            if i == n or int(inp[n]) == int(inp[i]):
                continue
            else:
                sums.append(int(inp[n]) + int(inp[i])) 

    return sums

todaysInput = open("input9.txt", "r")
#todaysInput = open("testInput8.txt", "r")
print("Name of the file: ", todaysInput.name)

lines = todaysInput.readlines()

preamble = []

inputs = []

eternaty = False

for line in lines:

    inputs.append(line)

# preamble = copy.deepcopy(inputs[:25])
# print("preamble: ", preamble)
# inputs = copy.deepcopy(inputs[25:])
#print("inputs: ", inputs)
tempSums = []

for i in range(25,len(inputs)):
    tempSums = getSums(inputs[(i-25): (i)])
    #if i < 30 : print("inoputs: ", inputs[(i-25): (i)])
    #if i < 30 : print("tempSums: ", tempSums)

    if int(inputs[i]) not in tempSums:
        print("nummer is faulty:", inputs[i])
        faulty = inputs[i]
        index = i
        break

testSum = 0
values = []

for i in range(0,index):

    for j in range(i,index): 

        testSum = testSum + int(inputs[j])
        values.append(inputs[j])
        if testSum == int(faulty):
            values.sort()
            print("Values: ", values)
            print("min Values: ", min(values))
            print("max Values: ", max(values))
            print("product: ", int(min(values))+int(max(values)))
        elif testSum > int(faulty):
            testSum = 0
            values = []


# for i in range(0,len(preamble)-1):
#     for n in range(0,len(preamble)-1):
#         if i == n or int(preamble[n]) == int(preamble[i]):
#             continue
#         else:
#             sums.append(int(preamble[n]) + int(preamble[i]))

# print("sums: ", sums)

# for nummer in inputs:
#     if int(nummer) not in sums:
#         print("nummer is faulty:", nummer)    

#print(commands)
#print(commands[place])

# while eternaty == False:
#     com = commands[place]
#     com = com.rstrip()

#     if "acc" in com:
#         if "+" in com:
#             accum = accum + int(com.split("+")[1])
#         else:
#             accum = accum - int(com.split("-")[1])

#         place = place + 1

#     elif "jmp" in com:
#         if "+" in com:
#             place = place + int(com.split("+")[1])
#         else:
#             place = place - int(com.split("-")[1])

#     elif "nop" in com:
#         place = place + 1

#     if place in visited:
#         eternaty = True
#         print("acc: " , accum)

#     else:
#         visited.append(place)

# Close opened file
todaysInput.close()