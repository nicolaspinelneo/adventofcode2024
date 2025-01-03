import re
import copy
import time
import math

# import sys
# sys.setrecursionlimit(15000)

startTime=time.time()

file1 = open('./2024/day20/testpyfile2.csv', 'r')
Lines = file1.readlines()

matrice=[]
for l, line in enumerate(Lines):
    line=line.strip()
    # print(line)
    # allNumbers = re.findall(r'\d+', line)
    # allNumbers=[int(x) for x in allNumbers]
    matrice.append(line)


    # allNumbers = re.findall(r'\d+', line)
    # allNumbers=[int(x) for x in allNumbers]
# G = [int(row) for row in line]
G = [[c for c in row] for row in matrice]
Gt = [[-1 for c in row] for row in matrice]
# G2 = [[c for c in row] for row in matrice]
# G3 = [[c for c in row] for row in matrice]

# PART ONE
count = 0
# for l in range(len(G)):
#     print(''.join(G[l]))

for l in range((len(G))):
    for c in range(len(G[0])):
        if(G[l][c])=="S":
            start=[l,c]
        elif(G[l][c])=="E":
            end=[l,c]

print("Start = {}".format(start))
print("End = {}".format(end))

dir=[[0,1],[1,0],[0,-1],[-1,0]]

curPos=start
Gt[curPos[0]][curPos[1]]=0
t=1
while(curPos!=end):
    for d in dir:
        if G[curPos[0]+d[0]][curPos[1]+d[1]] in [".","E"]:
            curPos=[curPos[0]+d[0],curPos[1]+d[1]]
            Gt[curPos[0]][curPos[1]]=t
            G[curPos[0]][curPos[1]]="X"
            t+=1
            break

# for l in range(len(G)):
#     print(''.join(G[l]))

nbcheat={}
for l in range((len(Gt))):
    for c in range(len(Gt[0])):
        if(Gt[l][c]==-1 and 0<l<len(Gt)-1 and 0<c<len(Gt[0])-1):
            cheat=-1
            if(Gt[l+dir[0][0]][c+dir[0][1]]>=0 and Gt[l+dir[2][0]][c+dir[2][1]]>=0):
                cheat=abs(Gt[l+dir[0][0]][c+dir[0][1]]-Gt[l+dir[2][0]][c+dir[2][1]])-2
            if(Gt[l+dir[1][0]][c+dir[1][1]]>=0 and Gt[l+dir[3][0]][c+dir[3][1]]>=0):
                cheat=abs(Gt[l+dir[1][0]][c+dir[1][1]]-Gt[l+dir[3][0]][c+dir[3][1]])-2
            if(cheat>=0):
                if(cheat>=100):
                    count+=1
                    if(cheat in nbcheat):
                        nbcheat[cheat]+=1
                    else:
                        nbcheat[cheat]=1

print(nbcheat)

# PART TWO
count2 = 0

# PART ONE
print("PART ONE : count = {}".format(count))
# 44 ???
# 7873 KO
# 5544 KO
# 5546 KO <=
# 5525 KO
# 1387

# PART TWO
print("PART TWO : count2 = {}".format(count2))
# ???


# bSym 4760 for iteration 7860

endTime=time.time()
print("Process time spent : {}s".format(round(endTime-startTime,2)))
