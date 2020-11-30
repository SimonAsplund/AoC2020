#!/usr/bin/python3

# Open a file
todaysInput1 = open("input1.txt", "r")
print("Name of the file: ", todaysInput1.name)

lines = todaysInput1.readlines()

for line in lines:
    # Do stuff
    print(line)
# Close opened file
todaysInput1.close()
