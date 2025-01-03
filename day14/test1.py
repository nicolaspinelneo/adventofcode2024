import re
import copy
import time
import math

startTime=time.time()

file1 = open('./2024/day14/testpyfile2.csv', 'r')
Lines = file1.readlines()

# matrice=[]

robots=[]
for line in Lines:
    line=line.strip()
    # print(line)
    # matrice.append(line)
    # allNumbers = re.findall(r'\d+', line)
    # allNumbers=[int(x) for x in allNumbers]
    allNumbers=line.split(" ")
    allNumbers=[[int(j) for j in i[2:].split(",")] for i in allNumbers]
    robots.append(allNumbers)
robots2=[[c for c in r] for r in robots]
# G = [int(row) for row in line]
# G = [[c for c in row] for row in matrice]
# G2 = [[c for c in row] for row in matrice]
# G3 = [[c for c in row] for row in matrice]
# print(robots)


# PART ONE
count = 0
tilex=0
tiley=0
for sec in range(100):
    for r in range(len(robots)):
        if robots[r][0][0]+1>tilex:
            tilex=robots[r][0][0]+1
        if robots[r][0][1]+1>tiley:
            tiley=robots[r][0][1]+1



def display(rob):
    G = [[0 for col in range(tilex)] for line in range(tiley)]
    for r in range(len(rob)):
        G[rob[r][0][1]][rob[r][0][0]]+=1
    for l in range(len(G)):
        ll=""
        for c in range(len(G[0])):
            ll+="." if G[l][c]==0 else str(G[l][c])
        print(ll)
    print("_"*20)

def checkSym(rob):
    G = [[0 for col in range(tilex)] for line in range(tiley)]
    nbSym=0
    for r in range(len(rob)):
        G[rob[r][0][1]][rob[r][0][0]]+=1
    for l in range(len(G)):
        for c in range(len(G[0])//2):
            if G[l][c]==0 and G[l][c]==G[l][tilex-c-1]:
                nbSym+=1
    return nbSym

# display(robots)

for sec in range(100):
    for r in range(len(robots)):
        robots[r][0]=[(robots[r][0][0]+robots[r][1][0]+tilex)%tilex, (robots[r][0][1]+robots[r][1][1]+tiley)%tiley]

# display(robots)

def getQuadrants(rob):
    quadrants=[0,0,0,0]
    for r in range(len(rob)):
        if(rob[r][0][0]<(tilex-1)/2 and rob[r][0][1]<(tiley-1)/2):
            quadrants[0]+=1
        elif(rob[r][0][0]>(tilex-1)/2 and rob[r][0][1]<(tiley-1)/2):
            quadrants[1]+=1
        elif(rob[r][0][0]>(tilex-1)/2 and rob[r][0][1]>(tiley-1)/2):
            quadrants[2]+=1
        elif(rob[r][0][0]<(tilex-1)/2 and rob[r][0][1]>(tiley-1)/2):
            quadrants[3]+=1
    print(quadrants)
    return quadrants

quadrants=getQuadrants(robots)
count=quadrants[0]*quadrants[1]*quadrants[2]*quadrants[3]

# PART TWO
count2 = 0

maxNbSym=0
for sec in range(7861):
    for r in range(len(robots2)):
        robots2[r][0]=[(robots2[r][0][0]+robots2[r][1][0]+tilex)%tilex, (robots2[r][0][1]+robots2[r][1][1]+tiley)%tiley]
    nbSym=checkSym(robots2)
    if nbSym>maxNbSym:
        maxNbSym=nbSym
        print("quadrants {}".format(getQuadrants(robots2)))
        print("nbSym {} for iteration {}".format(nbSym, sec))

display(robots2)

for r in range(len(robots2)):
    robots2[r][0]=[(robots2[r][0][0]+robots2[r][1][0]+tilex)%tilex, (robots2[r][0][1]+robots2[r][1][1]+tiley)%tiley]
display(robots2)

# PART ONE
print("PART ONE : count = {}".format(count))
# 229868730

# PART TWO
print("PART TWO : count2 = {}".format(count2))
# 7860 to low
# 7861

# bSym 4760 for iteration 7860

endTime=time.time()
print("Process time spent : {}s".format(round(endTime-startTime,2)))
