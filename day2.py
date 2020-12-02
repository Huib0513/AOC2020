#!python3
import os
import datetime

# input integers separated by commas
#input= [int(i) for i in open(os.path.basename(__file__).split(".")[0]+'.input').read().split(",")]

# input complete lines
#input = open(os.path.basename(__file__).split(".")[0]+'.input').read().splitlines()

input = open(os.path.basename(__file__).split(".")[0]+'.input').read().splitlines()


def getpolicy(text):
    policy = {}
    policy[text.split(" ")[1]] = (int(text.split(" ")[0].split("-")[0]), int(text.split(" ")[0].split("-")[1]))
    return policy

def matchespolicy1(text, policy):
    for key in policy:
        if ((text.count(key) >= policy[key][0]) & (text.count(key) <= policy[key][1])):
            return True
    return False

def matchespolicy2(text, policy):
    for key in policy:
        if ((text[policy[key][0]] == key) ^ (text[policy[key][1]] == key)):
            return True
    return False

def solve2():
    correct = 0
    for line in input:
        policy = getpolicy(line.split(":")[0])
        if (matchespolicy2(line.split(":")[1], policy)):
            correct +=1
    print("Aantal geldige wachtwoorden: " + str(correct))

def solve1():
    correct = 0
    for line in input:
        policy = getpolicy(line.split(":")[0])
        if (matchespolicy1(line.split(":")[1], policy)):
            correct +=1
    print("Aantal geldige wachtwoorden: " + str(correct))
    

start = datetime.datetime.now()
solve1()
end = datetime.datetime.now()
print("Tijd voor oplossing 1: ", end-start)

start = datetime.datetime.now()
solve2()
end = datetime.datetime.now()
print("Tijd voor oplossing 2: ", end-start)