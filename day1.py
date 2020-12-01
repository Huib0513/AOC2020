#!python3
import os

# input integers separated by commas
#start= [int(i) for i in open(os.path.basename(__file__).split(".")[0]+'.input').read().split(",")]

# input complete lines
#lines = open(os.path.basename(__file__).split(".")[0]+'.input').read().splitlines()

expenses = [int(x) for x in open(os.path.basename(__file__).split(".")[0]+'.input').read().splitlines()]
expenses.sort()

base = index1 = index2 = 0
while not (expenses[base] + expenses[index1] + expenses[index2] == 2020):
    index2 += 1
    if (index2 >= len(expenses)):
        index1 += 1
        index2 = index1
        if (index1 >= len(expenses)):
            base += 1
            index2 = index1 = base

print(expenses[base], expenses[index1], expenses[index2], expenses[base]*expenses[index1]*expenses[index2])

