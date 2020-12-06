#!/usr/bin/python3

# Open a file
from pexpect import runu

#3237 to High
#3225 to high
#3094 to high
#3042

todaysInput = open("input6.txt", "r")
#todaysInput = open("testInput6.txt", "r")
print("Name of the file: ", todaysInput.name)

lines = todaysInput.readlines()
empty = 0
yes = 0
answers = set()
Manswers = set()
VALID = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
newLine = 0


print("VALID: ", VALID)

for line in lines:

    newLine = newLine + 1
    print("line: ", line)

    if line == "/n" or not line.strip():
        empty = empty + 1


    print(line.rstrip())

    if len(answers) != 0 and empty == 0:
        for question in line:
            if question in VALID:
                Manswers.add(question)

        print("answers: ", answers)
        print("Manswers: ", Manswers)
        answers = answers & Manswers
        print("answers: ", answers)
        Manswers.clear()


    # first itteration
    elif newLine == 1:
        for question in line:
            if question in VALID:
                answers.add(question)

        print("FIRST answers: ", answers)

    if empty > 0:
        empty = 0
        print("Answears: ", len(answers))
        yes = yes + len(answers)
        print("YES: ", yes)
        answers.clear()
        Manswers.clear()
        newLine = 0

print("FINAL len(answers): ", answers)
print("FINAL len(Manswers): ", Manswers)

yes = yes + len(answers)
print("FINAL YES: ", yes)

# Close opened file
todaysInput.close()