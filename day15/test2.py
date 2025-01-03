import re
import copy
import time
import math

startTime=time.time()

file1 = open('./2024/day15/testpyfile2.csv', 'r')
Lines = file1.readlines()

matrice=[]
mdir=[]
isMat=True
for line in Lines:
    line=line.strip()
    # print(line)
    if(isMat==True and line==""):
        isMat=False
    else:
        if isMat==True:
            matrice.append(line)
        else:
            mdir.append(line)
    # allNumbers = re.findall(r'\d+', line)
    # allNumbers=[int(x) for x in allNumbers]
    # allNumbers=line.split(" ")
    # allNumbers=[[int(j) for j in i[2:].split(",")] for i in allNumbers]
# G = [int(row) for row in line]
G = [[c for c in row] for row in matrice]
Gdir = [[c for c in row] for row in mdir]
# G2 = [[c for c in row] for row in matrice]
# G3 = [[c for c in row] for row in matrice]

Gd=[]
for l in range(len(G)):
    Gd.append([])
    for c in range(len(G[0])):
        if(G[l][c]=="#"):
            Gd[l].append("#")
            Gd[l].append("#")
        elif(G[l][c]=="O"):
            Gd[l].append("[")
            Gd[l].append("]")
        elif(G[l][c]=="."):
            Gd[l].append(".")
            Gd[l].append(".")
        else:
            Gd[l].append("@")
            Gd[l].append(".")
        
G = [[c for c in row] for row in Gd]

# print(G)
# print(Gdir)

def displayMap(G):
    for l in range(len(G)):
        str=""
        for c in range(len(G[0])):
            str+=G[l][c]
        print(str)

displayMap(G)

# find robot
rc=-1
rl=-1
for l in range(len(G)):
    for c in range(len(G[0])):
        if G[l][c]=="@":
            rc=c
            rl=l
            break
    if(rc!=-1):
        break
# print("robot coord = {}, {}".format(rc, rl))

# move robot
d={">": [0,1],
   "v": [1,0],
   "<": [0,-1],
   "^": [-1,0]}

def getStonesToPush(horiz, l, c, dir):
    if horiz:
        if not (0<=l<len(G) and 0<=c<len(G[0])):
            return []
        if G[l][c] in ["[", "]"]:
            if G[l][c]=="]":
                return getStonesToPush(horiz, l+dir[0], c+dir[1], dir)
            else:
                return [[l,c]]+getStonesToPush(horiz, l+dir[0], c+dir[1], dir)
        return []
    else:
        if not (0<=l<len(G) and 0<=c<len(G[0])):
            return []
        if G[l][c] in ["[", "]"]:
            if G[l][c]=="]":
                return [[l,c-1]]+getStonesToPush(horiz, l+dir[0], c+dir[1]-1, dir)+getStonesToPush(horiz, l+dir[0], c+dir[1], dir)
            else:
                return [[l,c]]+getStonesToPush(horiz, l+dir[0], c+dir[1], dir)+getStonesToPush(horiz, l+dir[0], c+dir[1]+1, dir)
        return []
    
def isPushable(horiz, toPush, dir):
    if horiz:
        mi=10**9
        ma=-1
        for tp in toPush:
            mi=min(mi, tp[1])
            ma=max(ma, tp[1])
        if(dir[1]==1):
            return G[toPush[0][0]][ma+2]=="."
        else:
            return G[toPush[0][0]][mi-1]=="."
    else:
        for tp in toPush:
            if (G[tp[0]+dir[0]][tp[1]]=="#" or G[tp[0]+dir[0]][tp[1]+1]=="#"):
                return False
        return True

def push(horiz, toPush, dir):
    for tp in toPush:
        G[tp[0]][tp[1]]="."
        G[tp[0]][tp[1]+1]="."
    for tp in toPush:
        G[tp[0]+dir[0]][tp[1]+dir[1]]="["
        G[tp[0]+dir[0]][tp[1]+dir[1]+1]="]"

for ll in range(len(Gdir)):
    for cc in range(len(Gdir[0])):
        # print(d.get(Gdir[ll][cc]))
        nextCaseContent=G[rl+d.get(Gdir[ll][cc])[0]][rc+d.get(Gdir[ll][cc])[1]]
        if nextCaseContent==".":
            # move
            G[rl][rc]="."
            rl+=d.get(Gdir[ll][cc])[0]
            rc+=d.get(Gdir[ll][cc])[1]
            G[rl][rc]="@"
            # displayMap(G)
            # print("check")
        # elif nextCaseContent=="#":
        #     # dont move
        #     print("dont move")
        elif nextCaseContent!="#":
            # push if possible
            # print("push")
            foundEmptySpace=False

            horiz=d.get(Gdir[ll][cc])[0]==0
            stToPush=getStonesToPush(horiz, rl+d.get(Gdir[ll][cc])[0], rc+d.get(Gdir[ll][cc])[1], d.get(Gdir[ll][cc]))
            print(stToPush)
            if isPushable(horiz, stToPush, d.get(Gdir[ll][cc])):
                print("Pushable !")
                push(horiz, stToPush, d.get(Gdir[ll][cc]))
                # and move robot finally!
                G[rl][rc]="."
                rl+=d.get(Gdir[ll][cc])[0]
                rc+=d.get(Gdir[ll][cc])[1]
                G[rl][rc]="@"
                # displayMap(G)
                # print("check")
            else:
                print("Not pushable")
        # displayMap(G)
        # time.sleep(1)

            # nbStone=0
            # sl=rl+d.get(Gdir[ll][cc])[0]*2
            # sc=rc+d.get(Gdir[ll][cc])[1]*2
            # nextStone=G[sl][sc]
            # while(0<=sl<len(G) and 0<=sc<len(G[0]) and (G[sl][sc] in ["[","]"])):
            #     sl+=d.get(Gdir[ll][cc])[0]
            #     sc+=d.get(Gdir[ll][cc])[1]
            # if 0<=sl<len(G) and 0<=sc<len(G[0]):
            #     if(G[sl][sc]=="."):
            #         # print("can push {} !".format(max(abs(sl-rl),abs(sc-rc))-1))
            #         for iter in range(max(abs(sl-rl),abs(sc-rc))-1):
            #             G[sl][sc]=G[sl-d.get(Gdir[ll][cc])[0]][sc-d.get(Gdir[ll][cc])[1]]
            #             sl-=d.get(Gdir[ll][cc])[0]
            #             sc-=d.get(Gdir[ll][cc])[1]
            #         # and move robot finally!
            #         G[rl][rc]="."
            #         rl+=d.get(Gdir[ll][cc])[0]
            #         rc+=d.get(Gdir[ll][cc])[1]
            #         G[rl][rc]="@"


        # print("robot coord = {}, {}".format(rl, rc))

displayMap(G)

# PART ONE
count = 0


# PART TWO
count2 = 0

for l in range(len(G)):
    for c in range(len(G[0])):
        if G[l][c]=="[":
            count2+=c+l*100

# PART ONE
print("PART ONE : count = {}".format(count))
# 1479679

# PART TWO
print("PART TWO : count2 = {}".format(count2))
# 1509780


# bSym 4760 for iteration 7860

endTime=time.time()
print("Process time spent : {}s".format(round(endTime-startTime,2)))
