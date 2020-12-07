#!python3
import os
import datetime
from collections import defaultdict

# Test input
#input = ["abc","","a","b","c","","ab","ac","","a","a","a","a","","b", ""]

# input integers separated by commas
#input= [int(i) for i in open(os.path.basename(__file__).split(".")[0]+'.input').read().split(",")]

# input complete lines
input = open(os.path.basename(__file__).split(".")[0]+'.input').read().splitlines()

       
def solve1():
    group = 0
    groups = []
    groups.append(defaultdict(int))
    for line in input:
        if len(line) == 0:
            group += 1
            groups.append(defaultdict(int))
            continue
        for l in line:
            groups[group][l] += 1 
    print(sum([len(x) for x in groups]))

def solve2():
    result = 0
    group = []
    
    for line in range(len(input)):
        if len(input[line]) == 0:
            print("voor deze group (",group,") waren er ", len(set.intersection(*group)))
            result += len(set.intersection(*group))
            group = []
            continue
            
        group.append(set(input[line]))
    print("Resultaat deel 2: ", result)

start = datetime.datetime.now()
solve1()
print("Tijd voor oplossing 1: ", datetime.datetime.now()-start)

start = datetime.datetime.now()
solve2()
print("Tijd voor oplossing 2: ", datetime.datetime.now()-start)