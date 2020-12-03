#!python3
import os
import datetime

# Test input
# #input = ["..##.......","#...#...#..",".#....#..#.","..#.#...#.#",".#...##..#.","..#.##.....",".#.#.#....#",".#........#","#.##...#...","#...##....#",".#..#...#.#"]

# input integers separated by commas
#input= [int(i) for i in open(os.path.basename(__file__).split(".")[0]+'.input').read().split(",")]

# input complete lines
input = open(os.path.basename(__file__).split(".")[0]+'.input').read().splitlines()

def solve2():
    x = trees = 0
    totaltrees = 1
    for offset in [(1,1), (3,1), (5,1), (7,1), (1,2)]:
        y = offset[1]
        while y < len(input):
            x = ((x+offset[0]) % len(input[0]))
            #print("Checking (", x, ", ", y, ")")
            if (input[y][x] == '#'):
                trees += 1
            y += offset[1]
        print("Aantal bomen for offset", offset, ": ", trees)
        totaltrees *= trees
        x = trees = 0
        y = 1
    print("Oplossing 2: ", totaltrees)

def solve1():
    x = trees = 0
    y = 1
    while y < len(input):
        x = ((x+3) % len(input[0]))
        #print("Checking (", x, ", ", y, ")")
        if (input[y][x] == '#'):
            trees += 1
        y += 1
    print("Aantal bomen: ", trees)


start = datetime.datetime.now()
solve1()
end = datetime.datetime.now()
print("Tijd voor oplossing 1: ", end-start)

start = datetime.datetime.now()
solve2()
end = datetime.datetime.now()
print("Tijd voor oplossing 2: ", end-start)