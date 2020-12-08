#!python3
import os
import datetime
import re

# Test input
input = ["nop +0","acc +1","jmp +4","acc +3","jmp -3","acc -99","acc +1","jmp -4","acc +6"]
# input integers separated by commas
#input= [int(i) for i in open(os.path.basename(__file__).split(".")[0]+'.input').read().split(",")]

# input complete lines
input = open(os.path.basename(__file__).split(".")[0]+'.input').read().splitlines()

def nop(ip, accu, var):
    return ip+1, accu

def acc(ip, accu, var):
    return ip+1, accu+var

def jmp(ip, accu, var):
    return ip + var, accu

processor = {"nop": nop, "acc": acc, "jmp": jmp}

def solve1():
    ip = accu = 0
    oldips = []

    while not ip in oldips:
        oldips.append(ip)
        ip, accu = processor[program[ip][0]](ip, accu, int(program[ip][1]))
    print("Deel 1: ", accu)

def runit(program):
    ip = accu = 0
    done = False
    oldips = []

    while True:
        if ip == len(program):
            done = True
            #print("Finished with value: ", accu)
            break

        if not ip in oldips:
            oldips.append(ip)
            ip, accu = processor[program[ip][0]](ip, accu, int(program[ip][1]))
        else:
            #print("Looped with value: ", accu)
            break
    return done, accu

def solve2():
    done = False
    accu = 0

    for line in range(len(program)):
        if program[line][0] != "acc":
            print(line)
            attempt = program.copy()
            if attempt[line][0] == "jmp": 
                attempt[line] = ("nop", attempt[line][1])
            else:
                attempt[line] = ("jmp", attempt[line][1])
            
            done, accu = runit(attempt)

            if done:
                print("Deel 2: ", accu)
                break

program = [(line.split(" ")[0], line.split(" ")[1]) for line in input]
start = datetime.datetime.now()
solve1()
print("Tijd voor oplossing 1: ", datetime.datetime.now()-start)

start = datetime.datetime.now()
solve2()
print("Tijd voor oplossing 2: ", datetime.datetime.now()-start)