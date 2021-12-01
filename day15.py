#!python3
import os
import datetime
from collections import defaultdict

# Test input
input = [0,3,6] # 436
#input = [1,3,2] # 1
#input = [2,1,3] # 10
#input = [1,2,3] # 27
#input = [2,3,1] # 78
#input = [3,2,1] # 438
#input = [3,1,2] # 1836

# Real input
#input = [6,13,1,15,2,0]

def solve1():
    print(input)
    solution = input.copy()
    solution.reverse()
    while (len(solution) < 2020):
        if solution[0] in solution[1:]:
#            print("found ", solution[0], " on index ",solution[1:].index(solution[0]), " in list ", solution[1:], " --> ", len(solution)-(len(solution)-solution[1:].index(solution[0])-1))
            solution.insert(0, len(solution)-(len(solution)-solution[1:].index(solution[0])-1))
        else:
            solution.insert(0, 0)

    print("Deel 1: ", solution[0])

def solve2():
    print(input)
    solution = defaultdict(lambda x: x)
    solution = {y:x for x,y in enumerate(input)}
    last = input[len(input)-1]
    print(solution)
    for i in range(len(solution), 30000000):
        if i == 2020:
            print("Deel 1:", "No")
            break
#    while (len(solution) < 30000000):
#        if solution[0] in solution[1:]:
#            print("found ", solution[0], " on index ",solution[1:].index(solution[0]), " in list ", solution[1:], " --> ", len(solution)-(len(solution)-solution[1:].index(solution[0])-1))
#            solution.insert(0, len(solution)-(len(solution)-solution[1:].index(solution[0])-1))
#        else:
#            solution.insert(0, 0)

    print("Deel 2: ", "No")

start = datetime.datetime.now()
solve1()
print("Tijd voor oplossing 1: ", datetime.datetime.now()-start)

start = datetime.datetime.now()
solve2()
print("Tijd voor oplossing 2: ", datetime.datetime.now()-start)