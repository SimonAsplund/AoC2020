#!/usr/bin/python3

# Open a file
from pexpect import runu

#228
#256
#353 to low

todaysInput1 = open("input.txt", "r")
print("Name of the file: ", todaysInput1.name)

lines = todaysInput1.readlines()

hitts = 0

for line in lines:

    #find min nr
    line = line.split("-",1)
    pos1 = int(line[0])

    pos2 = int(line[1].split(" ")[0])
    # 13-15 c: cqbhncccjsncqcc
    letter =  line[1].split(" ")[1].split(":", 1)[0]
    letters = line[1].split(" ")[2]

    if(letter == letters[pos1-1] and letter != letters[pos2-1] or letter != letters[pos1-1] and letter == letters[pos2-1]):
        hitts = hitts + 1
        print(pos1)
        print(pos2)

        print(letters[pos1-1])
        print(letters[pos2-1])

        print(letter)
        print(letters)



    #if nuberOfHits >= min and nuberOfHits <= max:
    #    hitts = hitts + 1
    #    print(min)
    #    print(max)
    #    print(nuberOfHits)
    #    print(letter)
    #    print(letters)

print(hitts)

# Close opened file
todaysInput1.close()
