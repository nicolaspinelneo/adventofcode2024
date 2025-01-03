import re
import copy
import time
import math

# import sys
# sys.setrecursionlimit(15000)

startTime=time.time()

file1 = open('./2024/day25/testpyfile2.csv', 'r')
Lines = file1.readlines()

pins=[]
keys=[]

def parseKeyofPin():
    G = [[c for c in row] for row in matrice]
    if matrice[0]=='#####':
        # this is a pin
        tempPin=[0,0,0,0,0]
        for c in range(len(G[0])):
            for l in range(1,len(G)):
                if G[l][c]=='#':
                    tempPin[c]+=1
                else:
                    break
        pins.append(tempPin)
    else:
        # this is a key
        tempKey=[0,0,0,0,0]
        for c in range(len(G[0])):
            for l in range(len(G)-2,-1,-1):
                if G[l][c]=='#':
                    tempKey[c]+=1
                else:
                    break
        keys.append(tempKey)
    

newPin=True
for l, line in enumerate(Lines):
    line=line.strip()
    # print(line)
    if newPin==True:
        newPin=False
        matrice=[]
        matrice.append(line)
    else:
        if line=="":
            newPin=True
            parseKeyofPin()
        else:
            matrice.append(line)

parseKeyofPin()

print(pins)
print(keys)

# PART ONE
count = 0

for p in pins:
    for k in keys:
        fit=True
        for i in range(len(k)):
            if k[i]+p[i]>5:
                fit=False
                break
        if fit:
            count+=1

# print(net)
# G = [int(row) for row in line]
# G = [[c for c in row] for row in matrice]
# G2 = [[c for c in row] for row in matrice]
# G3 = [[c for c in row] for row in matrice]



# PART TWO
count2 = 0

# PART ONE
print("PART ONE : count = {}".format(count))
# ???

# PART TWO
print("PART TWO : count2 = {}".format(count2))
# ???


endTime=time.time()
print("Process time spent : {}s".format(round(endTime-startTime,2)))
