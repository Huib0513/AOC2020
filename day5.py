#!python3
import os
import datetime

# Test input
#input = ["FBFBBFFRLR","BFFFBBFRRR","FFFBBBFRRR","BBFFBBFRLL"]

# input integers separated by commas
#input= [int(i) for i in open(os.path.basename(__file__).split(".")[0]+'.input').read().split(",")]

# input complete lines
input = open(os.path.basename(__file__).split(".")[0]+'.input').read().splitlines()

def splitit(rows, splits):
    if len(splits) == 0: return rows
    #print(rows, splits)
    if splits[0]=='F' or splits[0]=='L':
        return splitit(rows[:len(rows)//2], splits[1:])
    else:
        return splitit(rows[len(rows)//2:], splits[1:])
        
def solve2():
    ids = [splitit(list(range(128)), b[:7])[0]*8 + splitit(list(range(8)), b[7:])[0] for b in input]
    for seat in range(len(ids)):
        if seat not in ids and seat +1 in ids and seat - 1 in ids:
            print("Je zit op:", seat)

def solve1():
    #for boardingpass in input:
        #row = splitit(list(range(128)), boardingpass[:7])
        #print("Boarding pass: ", boardingpass, " is in row: ", row[0])
        #seat = splitit(list(range(8)), boardingpass[7:])
        #print("Boarding pass: ", boardingpass, " is in seat: ", seat[0])
        #print("Boarding pass: ", boardingpass, " has ID: ", row[0]*8 + seat[0])
    ids = [splitit(list(range(128)), b[:7])[0]*8 + splitit(list(range(8)), b[7:])[0] for b in input]
    print("Max ID is:", max(ids))


start = datetime.datetime.now()
solve1()
print("Tijd voor oplossing 1: ", datetime.datetime.now()-start)

start = datetime.datetime.now()
solve2()
print("Tijd voor oplossing 2: ", datetime.datetime.now()-start)