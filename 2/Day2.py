#!/usr/bin/python3

# Open a file
from pexpect import runu

todaysInput1 = open("input.txt", "r")
print("Name of the file: ", todaysInput1.name)

lines = todaysInput1.readlines()

hitts = 0

for line in lines:

    #find min nr
    line = line.split("-",1)
    min = int(line[0])

    max = int(line[1].split(" ")[0])
    # 13-15 c: cqbhncccjsncqcc
    letter =  line[1].split(" ")[1].split(":", 1)[0]
    letters = line[1].split(" ")[2]

    nuberOfHits = letters.count(letter)

    if nuberOfHits >= min and nuberOfHits <= max:
        hitts = hitts + 1
        print(min)
        print(max)
        print(nuberOfHits)
        print(letter)
        print(letters)

print(hitts)

# Close opened file
todaysInput1.close()
