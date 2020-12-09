#!python3
import os
import datetime
import re

# Test input
input = [35,20,15,25,47,40,62,55,65,95,102,117,150,182,127,219,299,277,309,576]
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

def solve1(offset):
    for i in range(offset, len(input)):
        if not findmatch(input[i], input[i-offset:i]):
            print("Deel 1: ", input[i])
            return(input[i])


def solve2(target):
    for number in range(1, len(input)-1):
        print("Looking for length ", number)
        start = 0

        while start < len(input):
            #print("Checking indexes ", start, " to ", start+number)
            if sum(input[start:start+number+1]) == target:
                print("Deel 2: ", min(input[start:start+number+1])+max(input[start:start+number+1]))
                return
            start += 1
    
    print("Deel 2: No")


start = datetime.datetime.now()
s1 = solve1(25)
print("Tijd voor oplossing 1: ", datetime.datetime.now()-start)

start = datetime.datetime.now()
solve2(s1)
print("Tijd voor oplossing 2: ", datetime.datetime.now()-start)