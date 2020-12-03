#!/usr/bin/python3

# Open a file
from pexpect import runu

#55
#57
#65
#191

todaysInput1 = open("input3.txt", "r")
print("Name of the file: ", todaysInput1.name)

val = [1, 3, 5, 7]

lines = todaysInput1.readlines()

tot = 1

for i in val:

    pos = 0

    tree = 0

    rad = 1

    print("i rad : ", i, rad)

    for line in lines:

        if "#" == line[pos]:
            tree = tree + 1

        #print(pos)
        #print(len(line))
        #print(line[pos])
        #print(line)

        pos = pos + i

        if pos >= 31:
            pos = pos - 31

        rad = rad + 1

    print('tree: ', tree)

    tot = tot * tree

print(tot)

pos = 0

tree = 0

rad = 1

for line in lines:

    if rad % 2 == 0:
        rad = rad + 1
        continue

    if "#" == line[pos]:
        tree = tree + 1

    # print(pos)
    # print(len(line))
    # print(line[pos])
    # print(line)

    pos = pos + 1

    if pos >= 31:
        pos = pos - 31

    rad = rad + 1

print('tree: ', tree)

tot = tot * tree
print(tot)
# Close opened file
todaysInput1.close()
