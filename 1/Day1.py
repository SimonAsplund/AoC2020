#!/usr/bin/python3

# Open a file
todaysInput1 = open("input1.txt", "r")
print("Name of the file: ", todaysInput1.name)

lines = todaysInput1.readlines()
summan = 2020

lines = [ int(l) for l in lines]

for line in lines:
    # Do stuff

    diff = summan - line

    if diff in lines:
      print(line)
      print(diff)
      print(line * diff)
# Close opened file
todaysInput1.close()
