#!python3
import os
import datetime
import re

# Test input
input = ["F10","N3","F7","R90","F11"]

# input integers separated by commas
#input= [int(i) for i in open(os.path.basename(__file__).split(".")[0]+'.input').read().split(",")]

# input complete lines
input = open(os.path.basename(__file__).split(".")[0]+'.input').read().splitlines()

def solve1():
    pos = {'x':0, 'y':0}
    compass = ["E", "S", "W", "N"]
    dirs = {"E": ('x', 1), "S": ('y', -1), "W": ('x', -1), "N": ('y', 1)}
 
    direction = 'E'
    steps = [(i[0], int(i[1:])) for i in input]
    print(steps)
    for s in steps:
        if s[0] == 'R' or s[0] == "L":
            direction = compass[(compass.index(direction) + (s[1]//90) * 1 if s[0] == "R" else -1)%len(compass)]
            continue
        if s[0] == 'F':
            pos[dirs[direction][0]] += s[1] * dirs[direction][1]
        else:
            pos[dirs[s[0]][0]] += s[1] * dirs[s[0]][1]
    print("Deel 1: ", pos, abs(pos['x']) + abs(pos['y']))

def solve2():
    print("Deel 2: No")

start = datetime.datetime.now()
solve1()
print("Tijd voor oplossing 1: ", datetime.datetime.now()-start)

start = datetime.datetime.now()
solve2()
print("Tijd voor oplossing 2: ", datetime.datetime.now()-start)