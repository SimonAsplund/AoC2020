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

validEyeC = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
okPID = set('0123456789')

for line in lines:

    if line == "/n" or not line.strip():
        empty = empty + 1
        print("empty", empty)

    print(line.rstrip())

    if "byr" in line:
        year = int(line.split("byr:")[1].split(" ")[0])
        print("Birth year: ", year)
        if 1920 <= int(year) <= 2002:
            print("YES VALID B YEAR: ", year)
            Birth = True

    if "iyr" in line:
        year = int(line.split("iyr:")[1].split(" ")[0])
        print("Issue year: ", year)
        if 2010 <= int(year) <= 2020:
            print("YES VALID I YEAR: ", year)
            Issue = True

    if "eyr" in line:
        year = int(line.split("eyr:")[1].split(" ")[0])
        print("Expiration year: ", year)
        if 2020 <= int(year) <= 2030:
            print("YES VALID E YEAR: ", year)
            Expiration = True

    if "hgt" in line:
        higth = line.split("hgt:")[1]
        print("Heigth 1: ", higth)

        if "cm" in higth:
            higthi = higth.split("cm")[0]
            print("Heigth 2: ", higthi)
            print("Heigth len: ", len(higthi))
            if len(higthi) < 4:
                Height = 150 <= int(higthi) <= 193
                print("Height ", higthi, " is: ", Height)

        elif "in" in higth:
            higthi = higth.split("in")[0]
            print("Heigth 2: ", higthi)
            print("Heigth len: ", len(higthi))
            if len(higthi) < 4:
                Height = 59 <= int(higthi) <= 76
                print("Height ", higthi, " is: ", Height)

    if "hcl" in line:
        hairC = line.split("hcl:")[1]
        print("Hair code: ", hairC)
        if hairC[0] != "#":
            print("Wrong color: ", hairC)
            Hair = False

        else:
            colorCode = hairC.split("#")[1].split(" ")[0].strip()
            print("CC: ", colorCode, "  len:", len(colorCode))
            if len(colorCode) != 6:
                Hair = False
            else:
                ok = set('0123456789abcdefABCDEFG')
                if set(colorCode).issubset(ok):
                    Hair = True

                print("Hair ", colorCode, " is: ", Hair)

    if "ecl" in line:
        valid = 0;
        eyeC = line.split("ecl:")[1].split(" ")[0].strip()
        print("EYE COLOR: ", eyeC)
        for c in validEyeC:
            if c in eyeC:
                valid = valid + 1

        Eye = valid == 1
        print("EYE ", eyeC, " is: ", Eye)

    if "pid" in line:
        pidN = line.split("pid:")[1].split(" ")[0].strip()
        Passport = set(pidN).issubset(okPID) and len(pidN) == 9
        print("PID ", pidN, " is: ", Passport)

    #Country = "cid" in line or True
    Country = True
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
