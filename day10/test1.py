import re
import copy
import time

startTime=time.time()

file1 = open('./2024/day10/testpyfile2.csv', 'r')
Lines = file1.readlines()

matrice=[]
for line in Lines:
    line=line.strip()
    # print(line)
    matrice.append(line)
    # allNumbers = re.findall(r'\d+', line)
    # allNumbers=[int(x) for x in allNumbers]
# G = [int(row) for row in line]
G = [[int(c) for c in row] for row in matrice]
# G2 = [[c for c in row] for row in matrice]
# G3 = [[c for c in row] for row in matrice]
# print(G)

# PART ONE
count = 0
startPos=[]
# find all start
for l in range(len(G)):
    for c in range(len(G[0])):
        if G[l][c]==0:
            startPos.append([l, c])
# print(startPos)

alreadyfound=[]

def countNbRec(cp, d):
    dir=[[1, 0], [0, 1], [-1, 0], [0, -1]]
    if(0<=cp[0]+dir[d][0]<len(G) and 0<=cp[1]+dir[d][1]<len(G[0])):
        newcp=[cp[0]+dir[d][0], cp[1]+dir[d][1]]
        if(G[newcp[0]][newcp[1]]==G[cp[0]][cp[1]]+1):
            if(G[newcp[0]][newcp[1]]==9):
                if(newcp in alreadyfound):
                    return 0
                else:
                    alreadyfound.append(newcp)
                    # print("found : {}".format(newcp))
                    return 1
            else:
                return countNbRec(newcp,0)+countNbRec(newcp,1)+countNbRec(newcp,2)+countNbRec(newcp,3)
        else:
            return 0
    else:
        return 0

def countNbRec2(cp, d):
    dir=[[1, 0], [0, 1], [-1, 0], [0, -1]]
    if(0<=cp[0]+dir[d][0]<len(G) and 0<=cp[1]+dir[d][1]<len(G[0])):
        newcp=[cp[0]+dir[d][0], cp[1]+dir[d][1]]
        if(G[newcp[0]][newcp[1]]==G[cp[0]][cp[1]]+1):
            if(G[newcp[0]][newcp[1]]==9):
                if(newcp in alreadyfound):
                    return 1
                else:
                    alreadyfound.append(newcp)
                    # print("found : {}".format(newcp))
                    return 1
            else:
                return countNbRec2(newcp,0)+countNbRec2(newcp,1)+countNbRec2(newcp,2)+countNbRec2(newcp,3)
        else:
            return 0
    else:
        return 0

# for each startingpos:
for startid in range(len(startPos)):
    currentPos=startPos[startid]
    # print(currentPos)
    alreadyfound=[]
    nbfound=countNbRec(currentPos,0)+countNbRec(currentPos,1)+countNbRec(currentPos,2)+countNbRec(currentPos,3)
    count+=nbfound
    # print("nb found : {}".format(nbfound))

# PART TWO
count2 = 0
for startid in range(len(startPos)):
    currentPos=startPos[startid]
    # print(currentPos)
    alreadyfound=[]
    nbfound=countNbRec2(currentPos,0)+countNbRec2(currentPos,1)+countNbRec2(currentPos,2)+countNbRec2(currentPos,3)
    count2+=nbfound
    # print("nb found : {}".format(nbfound))

# PART ONE
print("PART ONE : count = {}".format(count))
# ???


# PART TWO
print("PART TWO : count2 = {}".format(count2))
# ???

endTime=time.time()
print("Process time spent : {}s".format(round(endTime-startTime,2)))
