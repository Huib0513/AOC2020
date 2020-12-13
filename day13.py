#!python3
import os
import datetime
import re

# Test input
input = ["939","7,13,x,x,59,x,31,19"]

# input integers separated by commas
#input= [int(i) for i in open(os.path.basename(__file__).split(".")[0]+'.input').read().split(",")]

# input complete lines
input = open(os.path.basename(__file__).split(".")[0]+'.input').read().splitlines()

def solve1():
    buses = {x:y for (x,y) in [(int(x)-(timestamp % int(x)), int(x)) for x in input[1].split(",") if x.isnumeric()]}
    print("Deel 1: ", (min(buses) * buses[min(buses)]))

def solve2():
    print("Deel 2: No")

timestamp = int(input[0])
start = datetime.datetime.now()
solve1()
print("Tijd voor oplossing 1: ", datetime.datetime.now()-start)

start = datetime.datetime.now()
solve2()
print("Tijd voor oplossing 2: ", datetime.datetime.now()-start)