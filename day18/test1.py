import re
import copy
import time
import math

# import sys
# sys.setrecursionlimit(15000)

startTime=time.time()

file1 = open('./2024/day18/testpyfile1.csv', 'r')
Lines = file1.readlines()

size=7
# size=71
end=[size-1,size-1]
G = [["." for c in range(size)] for row in range(size)]

# matrice=[]
nbCorrupted=12
# nbCorrupted=1024
dataCorrupted=[]
nb=0
for line in Lines:
    line=line.strip()
    print(line)
    allNumbers = re.findall(r'\d+', line)
    allNumbers=[int(x) for x in allNumbers]
    dataCorrupted.append(allNumbers)

    if nb<nbCorrupted:
        G[allNumbers[1]][allNumbers[0]]="#"
        nb+=1

    # matrice.append(line)
    

    # allNumbers = re.findall(r'\d+', line)
    # allNumbers=[int(x) for x in allNumbers]
# G = [int(row) for row in line]
# G = [[c for c in row] for row in matrice]
# G2 = [[c for c in row] for row in matrice]
# G3 = [[c for c in row] for row in matrice]


def display(x):
    for l in range(len(G)):
        print(''.join([str(y) for y in x[l]]))

display(G)

Gp = [[-1 for c in range(size)] for row in range(size)]
dir=[[0,1],[1,0],[0,-1],[-1,0]]

found=False
heads=[[0,0]]
Gp[0][0]=0
while(not found):
    newheads=[]
    for h in heads:
        for d in dir:
            if(0<=h[0]+d[0]<size and 0<=h[1]+d[1]<size and G[h[0]+d[0]][h[1]+d[1]]=="." and Gp[h[0]+d[0]][h[1]+d[1]]==-1):
                Gp[h[0]+d[0]][h[1]+d[1]]=Gp[h[0]][h[1]]+1
                newheads.append([h[0]+d[0],h[1]+d[1]])
    if end in newheads:
        found=True
    else:
        heads=copy.copy(newheads)

display(Gp)

# PART ONE
count = Gp[end[0]][end[1]]

# PART TWO
count2 = 0

# PART ONE
print("PART ONE : count = {}".format(count))
# ???

# PART TWO
print("PART TWO : count2 = {}".format(count2))
# ???


# bSym 4760 for iteration 7860

endTime=time.time()
print("Process time spent : {}s".format(round(endTime-startTime,2)))
