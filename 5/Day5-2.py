#!/usr/bin/python3

# Open a file
from pexpect import runu

#F means "front", B means "back", L means "left", and R means "right".q

todaysInput = open("input5.txt", "r")
#todaysInput = open("testInput.txt", "r")
print("Name of the file: ", todaysInput.name)

lines = todaysInput.readlines()

rows = []

for i in range(0, 128):
    rows.append(i)

savedRows = rows
savedColumns = [0, 1, 2, 3, 4, 5, 6, 7]

IDs = []

print(rows)

for line in lines:

    rows = savedRows
    columns = savedColumns

    for clue in line:
        print(clue)
        rowsL = len(rows)
        middleRow = rowsL // 2

        columnsL = len(columns)
        middleColumns = columnsL // 2

        if clue == 'F':
            rows = rows[:middleRow]
            #print("Rows: ", rows)

        elif clue == 'B':
            rows = rows[middleRow:]
            #print("Rows: ", rows)
        elif clue == 'L':
            columns = columns[:middleColumns]
            #print("columns: ", columns)

        elif clue == 'R':
            columns = columns[middleColumns:]
            #print("columns: ", columns)

    print("Row: ", rows)
    print("columns: ", columns)
    tot = int(rows[0]) * 8 + int(columns[0])
    print("tot: ", tot)
    IDs.append(tot)

print("max ID: ", max(IDs))
IDs.sort()
print(IDs)
for i in range(6, 813):
    if i not in IDs:
        print("Not in IDS: ", i)
        # Close opened file
todaysInput.close()
