#!/usr/bin/python3

# Open a file
from pexpect import runu

#5710 to low

todaysInput = open("input6.txt", "r")
#todaysInput = open("testInput6.txt", "r")
print("Name of the file: ", todaysInput.name)

lines = todaysInput.readlines()
empty = 0
yes = 0
answers = {}
VALID = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

print("VALID: ", VALID)

for line in lines:

    print("line: ", line)

    if line == "/n" or not line.strip():
        empty = empty + 1
        print("empty", empty)

    print(line.rstrip())

    for question in line:
        if question in VALID:
            print("question: ", question)
            answers[question] = True

    if empty > 0:
        empty = 0
        print("Answears: ", len(answers))
        yes = yes + len(answers)
        answers = {}
        print("YES: ", yes)

yes = yes + len(answers)
print("FINAL YES: ", yes)

# Close opened file
todaysInput.close()