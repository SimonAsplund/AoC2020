#!/usr/bin/python3

# Open a file
from pexpect import runu

# 105 to low
# 229 to low

empty = 0
correct = 0

Birth = False
Issue = False
Expiration = False
Height = False
Hair = False
Eye = False
Passport = False
Country = False

todaysInput1 = open("input4.txt", "r")
print("Name of the file: ", todaysInput1.name)

lines = todaysInput1.readlines()

for line in lines:

    if line == "/n" or not line.strip():
        empty = empty + 1
        print("empty", empty)

    print(line.rstrip())

    Birth = "byr" in line or Birth
    if Birth:
        line.split("byr:")[1]
    Issue = "iyr" in line or Issue
    Expiration = "eyr" in line or Expiration
    Height = "hgt" in line or Height
    Hair = "hcl" in line or Hair
    Eye = "ecl" in line or Eye
    Passport = "pid" in line or Passport
    Country = "cid" in line or True

    all = Birth and Issue and Expiration and Height and Hair and Eye and Passport and Country

    if empty > 0 or all:
        if Birth and Issue and Expiration and Height and Hair and Eye and Passport and Country:
            print("! ! ! C O R R E C T ! ! !")
            correct = correct + 1
        print("New ID")
        Birth = False
        Issue = False
        Expiration = False
        Height = False
        Hair = False
        Eye = False
        Passport = False
        Country = False
        empty = 0

print("correct: ", correct)

# Close opened file
todaysInput1.close()
