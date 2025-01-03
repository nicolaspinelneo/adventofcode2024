import re
import copy
import time
import math

# import sys
# sys.setrecursionlimit(15000)

startTime=time.time()

file1 = open('./2024/day24/testpyfile2.csv', 'r')
Lines = file1.readlines()

dico={}
ope=[]
firstPart=True
for l, line in enumerate(Lines):
    line=line.strip()
    print(line)
    if line=="":
        firstPart=False
    else:
        if firstPart:
            line=line.replace(": ",";")
            couple=line.split(";")
            dico[couple[0]]=int(couple[1])
        else:
            quinte=line.split(" ")
            ope.append([quinte[0],quinte[1],quinte[2],quinte[4]])

for d in dico.keys():
    print("{}:{}".format(d, dico[d]))

opeComputed=0
opeSeen=[]
while(opeComputed<len(ope)):
    for i, o in enumerate(ope):
        if o[0] in dico and o[2] in dico:
            if(not i in opeSeen):
                if o[1]=="AND":
                    dico[o[3]]=dico[o[0]] and dico[o[2]]
                elif o[1]=="OR":
                    dico[o[3]]=dico[o[0]] or dico[o[2]]
                elif o[1]=="XOR":
                    dico[o[3]]=dico[o[0]] ^ dico[o[2]]
                print(dico[o[3]])
                opeSeen.append(i)
                opeComputed+=1




# print(net)
# G = [int(row) for row in line]
# G = [[c for c in row] for row in matrice]
# G2 = [[c for c in row] for row in matrice]
# G3 = [[c for c in row] for row in matrice]


# PART ONE
count = 0

toOrder=list(dico.keys())
toOrder.sort()

for d in toOrder:
    print("{} : {}".format(d, dico[d]))
    if d[0]=="z":
        if dico[d]:
            # print("{} {} {} so add {}".format(dico[d], d[0], d[1:], 2**int(d[1:])))
            count+=2**int(d[1:])
        # print("{}:{}".format(d, dico[d]))


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
