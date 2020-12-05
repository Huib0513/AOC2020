#!python3
import os
import datetime
import re

# Test input
#input = ["ecl:gry pid:860033327 eyr:2020 hcl:#fffffd","byr:1937 iyr:2017 cid:147 hgt:183cm","","iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884","hcl:#cfa07d byr:1929","","hcl:#ae17e1 iyr:2013","eyr:2024","ecl:brn pid:760753108 byr:1931","hgt:179cm","","hcl:#cfa07d eyr:2025 pid:166559648","iyr:2011 ecl:brn hgt:59in"]
# Invalid passports part 2
#input = ["eyr:1972 cid:100","hcl:#18171d ecl:amb hgt:170 pid:186cm iyr:2018 byr:1926","","iyr:2019",\
#"hcl:#602927 eyr:1967 hgt:170cm","ecl:grn pid:012533040 byr:1946","",\
#"hcl:dab227 iyr:2012","ecl:brn hgt:182cm pid:021572410 eyr:2020 byr:1992 cid:277",\
#"","hgt:59cm ecl:zzz","eyr:2038 hcl:74454a iyr:2023","pid:3556412378 byr:2007"]

# Valid passports part 2
#input=["pid:087499704 hgt:74in ecl:grn iyr:2012 eyr:2030 byr:1980",
#"hcl:#623a2f",
#"",
#"eyr:2029 ecl:blu cid:129 byr:1989",
#"iyr:2014 pid:896056539 hcl:#a97842 hgt:165cm",
#"",
#"hcl:#888785",
#"hgt:164cm byr:2001 iyr:2015 cid:88",
#"pid:545766238 ecl:hzl",
#"eyr:2022",
#"",
#"iyr:2010 hgt:158cm hcl:#b6652a ecl:blu byr:1944 eyr:2021 pid:093154719"]

# input integers separated by commas
#input= [int(i) for i in open(os.path.basename(__file__).split(".")[0]+'.input').read().split(",")]

# input complete lines
input = open(os.path.basename(__file__).split(".")[0]+'.input').read().splitlines()
def validlength(text):
    m = re.search("[0-9]{2,3}cm|in", text)
    if m != None:
        if (((text[-2:] == "cm" and 150<=int(re.search("\A\d+", text).group())<=193)) or 
             (text[-2:] == "in" and 59<=int(re.search("\A\d+", text).group())<=76)): return True
    return False

mandatory = {"byr": lambda x: (len(x) == 4 and (re.match("[0-9]{4}", x)) != None) and 1920 <= int(x) <=2002,
             "iyr": lambda x: (len(x) == 4 and (re.match("[0-9]{4}", x)) != None) and 2010 <= int(x) <=2020, 
             "eyr": lambda x: (len(x) == 4 and (re.match("[0-9]{4}", x)) != None) and 2020 <= int(x) <=2030, 
#             "hgt": lambda x: (x.endswith('cm') and 150 <= int(x[:-2]) <= 193)
#                           or (x.endswith('in') and  59 <= int(x[:-2]) <=  76), 
             "hgt": lambda x: validlength(x), 
             "hcl": lambda x: (len(x) == 7 and (re.match("#[0-9a-f]{6}", x)) != None), 
             "ecl": lambda x: x in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"], 
             "pid": lambda x: (len(x) == 9 and (re.match("[0-9]{9}", x)) != None )}

def passports(text):
    passport = {}
    for line in text:
        if len(line) == 0:
            yield passport
            passport = {}
            continue
        passport.update(dict(combi.split(":") for combi in line.split(" ")))
    yield passport

def solve2():
    ok = 0
    for p in passports(input):
        valid = False
        if set(p.keys()).issuperset(set(mandatory.keys())):
            valid = True
            for key in mandatory:
#                print(key, p[key], mandatory[key](p[key]))
                valid = valid and mandatory[key](p[key])
#        print(valid)
        if valid: ok += 1
    print("Aantal goede: ", ok)

def solve1():
    ok = 0
    for p in passports(input):
        if set(p.keys()).issuperset(set(mandatory.keys())): 
            ok += 1
    print("Aantal goede: ", ok)


start = datetime.datetime.now()
solve1()
print("Tijd voor oplossing 1: ", datetime.datetime.now()-start)

start = datetime.datetime.now()
solve2()
print("Tijd voor oplossing 2: ", datetime.datetime.now()-start)