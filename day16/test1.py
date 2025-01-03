import re
import copy
import time
import math

import sys

sys.setrecursionlimit(15000)

startTime=time.time()

file1 = open('./2024/day16/testpyfile2.csv', 'r')
Lines = file1.readlines()

matrice=[]
for line in Lines:
    line=line.strip()
    print(line)
    matrice.append(line)
    # allNumbers = re.findall(r'\d+', line)
    # allNumbers=[int(x) for x in allNumbers]
# G = [int(row) for row in line]
G = [[c for c in row] for row in matrice]
# G2 = [[c for c in row] for row in matrice]
# G3 = [[c for c in row] for row in matrice]

# print(G)
# print(Gdir)

# for l in range(len(G)):
#     print(''.join(G[l]))

pos=[len(G)-2,1]
end=[1,len(G[0])-2]

dir=[[0,1],[1,0],[0,-1],[-1,0]]

curMinScore=10**9

def foundPath(pos, path, dd, score):
    score+=1
    if(G[pos[0]][pos[1]]=="E"):
        # found !
        global curMinScore
        if(score<curMinScore):
            curMinScore=score
        print("min {} found with score {}".format(curMinScore-1, score-1))
        return [True, path+[pos], score]
    elif(score>curMinScore):
        # too long !
        return [False, [], 0]
    elif(pos in path):
        # loop
        return [False, [], 0]
    elif (G[pos[0]][pos[1]]!="#"):
        tried=[]
        for d in range(len(dir)):
            newscore=score
            if((d+dd)%4!=dd):
            # if(d!=dd):
                newscore+=1000
            # tried.append(foundPath([pos[0]+dir[d][0], pos[1]+dir[d][1]], path+[pos], d, newscore))
            tried.append(foundPath([pos[0]+dir[(d+dd)%4][0], pos[1]+dir[(d+dd)%4][1]], path+[pos], (d+dd)%4, newscore))
        min=10**9
        tmin=-1
        for t in range(len(tried)):
            if(tried[t][0]==True and tried[t][2]<min):
                min=tried[t][2]
                tmin=t
        if(tmin!=-1):
            return [True, tried[tmin][1], min]
    return [False, [], 0]

# PART ONE
count = 0
path=foundPath(pos, [], -1, 0)
print("path : {}".format(path[2]-1))

for p in path[1]:
    G[p[0]][p[1]]="*"
for l in range(len(G)):
    print(''.join(G[l]))

# PART TWO
count2 = 0

# PART ONE
print("PART ONE : count = {}".format(count))
# 1479679

# PART TWO
print("PART TWO : count2 = {}".format(count2))
# ???


# bSym 4760 for iteration 7860

endTime=time.time()
print("Process time spent : {}s".format(round(endTime-startTime,2)))
