import re
import copy
import time

startTime=time.time()

file1 = open('./2024/day06/testpyfile.csv', 'r')
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
curC=c
curL=l
print("start at {},{}".format(curL,curC))

GwithTrace=[[G[j][i] for i in range(len(G))] for j in range(len(G[0]))]

goOut=False
dir=[[-1,0],[0,1],[1,0],[0,-1]]
curD=0
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
            count+=1
    else:
        goOut=True

# PART TWO
count2 = 0
    
# PART ONE
for l in range(len(GwithTrace)):
    line=[]
    for c in range(len(GwithTrace[0])):
        line.append(GwithTrace[l][c])
    print(line)
print("PART ONE : count = {}".format(count))
# ???

# PART TWO
print("PART TWO : count2 = {}".format(count2))
# ???

endTime=time.time()
print("Process time spent : {}s".format(round(endTime-startTime,2)))
