import re
import copy
import time

startTime=time.time()

file1 = open('./2024/day06/testpyfile2.csv', 'r')
Lines = file1.readlines()

# def func(param):
#     return False
    
matrice=[]
for line in Lines:
    line=line.strip()
    print(line)
    matrice.append(line)

G = [[c for c in row] for row in matrice]
print(G)

# PART ONE
count = 1
found=False
for l in range(len(G)):
    for c in range(len(G[0])):
        if(G[l][c]=="^"):
            found=True
            break
    if(found==True):
        break
curCStart=c
curLStart=l
print("start at {},{}".format(curLStart,curCStart))

# PART ONE
GwithTrace=[[G[j][i] for i in range(len(G))] for j in range(len(G[0]))]
goOut=False
dir=[[-1,0],[0,1],[1,0],[0,-1]]
curD=0
curC=curCStart
curL=curLStart
path=[]
while(not goOut):
    GwithTrace[curL][curC]=str(count%10)
    if(0<curL<len(G)-1 and 0<curC<len(G[0])-1):
        for d in range(len(dir)):
            if(G[curL+dir[(curD+d)%len(dir)][0]][curC+dir[(curD+d)%len(dir)][1]]!="#"):
                curD+=d
                curD=curD%len(dir)
                break
        curL+=dir[curD][0]
        curC+=dir[curD][1]
        if(GwithTrace[curL][curC]=="."):
            path.append([curL, curC])
            count+=1
    else:
        goOut=True

# PART TWO
count2 = 0

# for ll in range(len(G)):
#     for cc in range(len(G[0])):
showProgress=0
for p in range(len(path)):
    curC=curCStart
    curL=curLStart
    GwithNewObs=[[G[j][i] for i in range(len(G))] for j in range(len(G[0]))]

    # if(ll==6 and cc==3):
    # z=0

    GwithNewObs[path[p][0]][path[p][1]]="#"
    # if(GwithNewObs[ll][cc]!="#"):
    #     GwithNewObs[ll][cc]="#"
    # else:
    #     continue
    GwithTrace=[[GwithNewObs[j][i] for i in range(len(G))] for j in range(len(G[0]))]
    GwithDir=[[[] for i in range(len(G))] for j in range(len(G[0]))]


    goOut=False
    loop=False
    dir=[[-1,0],[0,1],[1,0],[0,-1]]
    curD=0
    countX = 1
    while(not goOut and not loop):
        GwithTrace[curL][curC]=str(countX%10)
        GwithDir[curL][curC].append(curD)
        if(0<curL<len(G)-1 and 0<curC<len(G[0])-1):
            for d in range(len(dir)):
                if(GwithNewObs[curL+dir[(curD+d)%len(dir)][0]][curC+dir[(curD+d)%len(dir)][1]]!="#"):
                    curD+=d
                    curD=curD%len(dir)
                    break
            curL+=dir[curD][0]
            curC+=dir[curD][1]
            if(GwithTrace[curL][curC]=="."):
                countX+=1
            else:
                if(curD in GwithDir[curL][curC]):
                    loop=True
                    count2+=1
                    if(showProgress==0):
                        print("found on {}, {} ({}/{})".format(path[p][0], path[p][1], p, (len(path))))
                    showProgress=(showProgress+1)%25
                    # for l in range(len(GwithTrace)):
                    #     line=[]
                    #     for c in range(len(GwithTrace[0])):
                    #         line.append(GwithTrace[l][c])
                    #     print(line)
        else:
            # print("OUT {}, {}".format(ll, cc))
            # for l in range(len(GwithTrace)):
            #     line=[]
            #     for c in range(len(GwithTrace[0])):
            #         line.append(GwithTrace[l][c])
            #     print(line)
            goOut=True

    
# PART ONE
# for l in range(len(GwithTrace)):
#     line=[]
#     for c in range(len(GwithTrace[0])):
#         line.append(GwithTrace[l][c])
#     print(line)
print("PART ONE : count = {}".format(count))
# 5080

# PART TWO
print("PART TWO : count2 = {}".format(count2))
# 1919

endTime=time.time()
print("Process time spent : {}s".format(round(endTime-startTime,2)))
