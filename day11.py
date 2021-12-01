#!python3
import os
import datetime
import re

# Test input
input = ["L.LL.LL.LL","LLLLLLL.LL","L.L.L..L..","LLLL.LL.LL","L.LL.LL.LL","L.LLLLL.LL","..L.L.....","LLLLLLLLLL","L.LLLLLL.L","L.LLLLL.LL"]

# input integers separated by commas
#input= [int(i) for i in open(os.path.basename(__file__).split(".")[0]+'.input').read().split(",")]

# input complete lines
#input = [ int(i) for i in open(os.path.basename(__file__).split(".")[0]+'.input').read().splitlines()]

def solve1():
    seating = []
    count = 0
    emptyrow = ""
    for x in range(len(input[0])): emptyrow = emptyrow + "."

    for row in range(len(input)):
        seating.append("." + input[row] + ".")

    seating.insert(0, emptyrow)
    seating.append(emptyrow)
    newseating = []

    while (newseating != seating) and (count <= 6):
        count += 1
        seating = newseating.copy()
        newseating = []
        for rownr in range(len(seating)):
            newrow = ""
            for seatnr in range(1,len(seating[rownr])-1):
                #print("Match (", rownr, ", ", seatnr, ")")
                if seating[rownr][seatnr] == "L":
                    #print("Match L")
                    if seating[rownr -1][seatnr-1:seatnr+1].count("#") + seating[rownr+1][seatnr-1:seatnr+1].count("#") + seating[rownr][seatnr-1:seatnr+1].count("#") == 0:
                        newrow += "#"
                    else: newrow += "L"
                elif seating[rownr][seatnr] == "#":
                    #print("Match #")
                    if seating[rownr -1][seatnr-1:seatnr+1].count("#") + seating[rownr+1][seatnr-1:seatnr+1].count("#") + seating[rownr][seatnr-1:seatnr+1].count("#") > 3:
                        newseating[rownr] += "L"
                    else:
                        newrow += "#"
                else:
                    newrow += "."
            newseating.append(newrow)
        print(count)
        print(seating)
        print(newseating)

    print("Deel 1: ", count)

def solve2():
    print("Deel 2: No")

start = datetime.datetime.now()
solve1()
print("Tijd voor oplossing 1: ", datetime.datetime.now()-start)

start = datetime.datetime.now()
solve2()
print("Tijd voor oplossing 2: ", datetime.datetime.now()-start)