#!python3
import os
import datetime
import re

# Test input
input = ["light red bags contain 1 bright white bag, 2 muted yellow bags.","dark orange bags contain 3 bright white bags, 4 muted yellow bags.",
    "bright white bags contain 1 shiny gold bag.","muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.",
    "shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.","dark olive bags contain 3 faded blue bags, 4 dotted black bags.",
    "vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.","faded blue bags contain no other bags.","dotted black bags contain no other bags."]

# input integers separated by commas
#input= [int(i) for i in open(os.path.basename(__file__).split(".")[0]+'.input').read().split(",")]

# input complete lines
input = open(os.path.basename(__file__).split(".")[0]+'.input').read().splitlines()

def splitline(line):
    splits = line.split(" bags contain ")
    color = splits[0]
    contains = sum([re.findall(r'(^\d) (\w+ \w+)', contents.strip()) for contents in splits[1].split(', ')], [])
    
    return (color, contains)

def maybecontainedin(bag, rules):
    direct = indirect = set()

    direct = set(r for r in rules if bag in [x[1] for x in rules[r]])
    for b in direct:
        indirect.update(maybecontainedin(b, rules))
    return direct.union(indirect)

def countbags(bag, rules):
    total = 1 + sum([int(b[0])*countbags(b[1], rules) for b in rules[bag]])
    #for b in rules[bag]:
    #    total += int(b[0])*countbags(b[1], rules)

    #print("Total for bag ", bag, ": ", total)
    return total

def solve1():
    bags = {}
    for (x,y) in [splitline(line) for line in input]:
        bags[x] = y

    print("Shiny gold may be contained in ", len(maybecontainedin("shiny gold", bags)), "bags !")

def solve2():
    bags = {}
    for (x,y) in [splitline(line) for line in input]:
        bags[x] = y

    print("Resultaat deel 2: ", countbags("shiny gold", bags)-1)

start = datetime.datetime.now()
solve1()
print("Tijd voor oplossing 1: ", datetime.datetime.now()-start)

start = datetime.datetime.now()
solve2()
print("Tijd voor oplossing 2: ", datetime.datetime.now()-start)