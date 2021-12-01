#!python3
import os
import datetime
import re

# Test input
#input = [16,10,15,5,1,11,7,19,6,12,4]
#input = [28,33,18,42,31,14,46,20,48,47,24,23,49,45,19,38,39,11,1,32,25,35,8,17,7,9,4,2,34,10,3]
# input integers separated by commas
#input= [int(i) for i in open(os.path.basename(__file__).split(".")[0]+'.input').read().split(",")]

# input complete lines
input = [ int(i) for i in open(os.path.basename(__file__).split(".")[0]+'.input').read().splitlines()]

def findmatch(s, input):
    for i in range(len(input)-1, 0, -1):
        for j in range(i):
            if input[i]+input[j] == s:
                return True

    return False

def solve1(input):
    diffs = [input[x+1]-input[x] for x in range(len(input)-1)]
    print("Deel 1: ", diffs.count(1)*(diffs.count(3)+1))

def solve2(target):
    print("Deel 2: No")

input.sort()
start = datetime.datetime.now()
s1 = solve1([0] + input)
print("Tijd voor oplossing 1: ", datetime.datetime.now()-start)

start = datetime.datetime.now()
solve2(s1)
print("Tijd voor oplossing 2: ", datetime.datetime.now()-start)