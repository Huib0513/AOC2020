#!python3
import os
import datetime

# input integers separated by commas
#input= [int(i) for i in open(os.path.basename(__file__).split(".")[0]+'.input').read().split(",")]

# input complete lines
#input = open(os.path.basename(__file__).split(".")[0]+'.input').read().splitlines()

input = [int(x) for x in open(os.path.basename(__file__).split(".")[0]+'.input').read().splitlines()]
input.sort()

def solve2():
    base = index1 = index2 = 0
    while not (input[base] + input[index1] + input[index2] == 2020):
        index2 += 1
        if (index2 >= len(input)):
            index1 += 1
            index2 = index1
            if (index1 >= len(input)):
                base += 1
                index2 = index1 = base

    print(input[base], input[index1], input[index2], input[base]*input[index1]*input[index2])

def solve1():
    base = index1 = 0
    while not (input[base] + input[index1] == 2020):
        index1 += 1
        if (index1 >= len(input)):
            base += 1
            index1 = base

    print(input[base], input[index1], input[base]*input[index1])

start = datetime.datetime.now()
solve1()
end = datetime.datetime.now()
print("Tijd voor oplossing 1: ", end-start)

start = datetime.datetime.now()
solve2()
end = datetime.datetime.now()
print("Tijd voor oplossing 2: ", end-start)