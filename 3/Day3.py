#!/usr/bin/python3

# Open a file
from pexpect import runu

#55
#57
#65

todaysInput1 = open("input3.txt", "r")
print("Name of the file: ", todaysInput1.name)

lines = todaysInput1.readlines()

pos = 0

tree = 0

rad = 1

for line in lines:

    print(rad)

    if "#" == line[pos]:
        print('#')
        tree = tree + 1

    #print(pos)
    #print(len(line))
    #print(line[pos])
    #print(line)

    pos = pos + 3

    if pos >= 31:
        pos = pos - 31

    rad = rad + 1

print(tree)

# Close opened file
todaysInput1.close()
