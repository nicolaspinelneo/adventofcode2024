import re
import copy
import time
import math

# import sys
# sys.setrecursionlimit(15000)

startTime=time.time()

file1 = open('./2024/day24/testpyfile2.csv', 'r')
Lines = file1.readlines()

permut=[["vkq","z11"],["qdq","pvb"],["mmk","z24"],["hqh","z38"]]

dico={}
ope=[]
firstPart=True
for l, line in enumerate(Lines):
    line=line.strip()
    # print(line)
    if line=="":
        firstPart=False
    else:
        if firstPart:
            line=line.replace(": ",";")
            couple=line.split(";")
            dico[couple[0]]=int(couple[1])
        else:
            quinte=line.split(" ")
            for p in permut:
                if quinte[4] in p:
                    if quinte[4]==p[0]:
                        quinte[4]=p[1]
                    else:
                        quinte[4]=p[0]
                    break
            ope.append([quinte[0],quinte[1],quinte[2],quinte[4]])

# for d in dico.keys():
#     print("{}:{}".format(d, dico[d]))


xValue=0
yValue=0
for d in dico:
    if d[0]=="x":
        if dico[d]:
            xValue+=2**int(d[1:])
    if d[0]=="y":
        if dico[d]:
            yValue+=2**int(d[1:])


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
                # print(dico[o[3]])
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
    # print("{} : {}".format(d, dico[d]))
    if d[0]=="z":
        if dico[d]:
            # print("{} {} {} so add {}".format(dico[d], d[0], d[1:], 2**int(d[1:])))
            count+=2**int(d[1:])
        # print("{}:{}".format(d, dico[d]))

actual=count
expect=xValue+yValue
print("xValue = {}".format(xValue))
print("yValue = {}".format(yValue))
print("actual zValue = {}".format(actual))
print("expect zValue = {}".format(expect))

greatNumber=max(actual,expect)
bitnb=0
while(greatNumber>0):
    if(actual%2!=expect%2):
        print("z{} KO <==".format(bitnb))
    # else:
    #     print("z{} OK".format(bitnb))
    bitnb+=1
    actual//=2
    expect//=2
    greatNumber//=2


# PART TWO
count2 = 0

def compute(x,y):
    for d in dico:
        if d[0]=="x":
            dico[d]=(x//2**int(d[1:]))%2
        if d[0]=="y":
            dico[d]=(y//2**int(d[1:]))%2

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
                    # print(dico[o[3]])
                    opeSeen.append(i)
                    opeComputed+=1

    computed=0
    for d in dico:
        if d[0]=="z":
            if dico[d]:
                # print("{} {} {} so add {}".format(dico[d], d[0], d[1:], 2**int(d[1:])))
                computed+=2**int(d[1:])
    actual=computed
    expect=x+y
    # print("actuel {} ".format(bin(actual)))
    # print("expect {} ".format(bin(expect)))
    greatNumber=max(computed,expect)
    bitnb=0
    errors=[]
    while(greatNumber>0):
        if(actual%2!=expect%2):
            # print("z{} KO <==".format(bitnb))
            errors.append("z"+str(100+bitnb)[1:])
        bitnb+=1
        actual//=2
        expect//=2
        greatNumber//=2
    return errors

print(compute(27133763813069,20654586710041))
# dicoErrors={}
# for x in range(0,1000):
#     for y in range(0,1000):
#         errors=compute(x,y)
#         for e in errors:
#             if e in dicoErrors:
#                 dicoErrors[e]+=1
#             else:
#                 dicoErrors[e]=1
# dicoErrorsSorted=list(dicoErrors.keys())
# dicoErrorsSorted.sort()
# for e in dicoErrorsSorted:
#     print("error {}, nb {}".format(e, dicoErrors[e]))

def dep(curOpe, alreadydep):
    r=[]
    for o in ope:
        if o[3]==curOpe:
            if not o[0] in alreadydep:
                r.append(o[0])
                alreadydep.append(o[0])
                r+=dep(o[0],alreadydep)
            if not o[2] in alreadydep:
                r.append(o[2])
                alreadydep.append(o[2])
                r+=dep(o[2],alreadydep)
        
    return r

def findDep():
    dicoDep={}
    for o in ope:
        if o[3][0]=="z":
            # if not o[3] in dicoDep:
            #     dicoDep[o[3]]=[]
            dicoDep[o[3]]=dep(o[3],[])
    return dicoDep

dependencies=findDep()
dicoDepSorted=list(dependencies.keys())
dicoDepSorted.sort()
for d in dicoDepSorted:
    print("bit {} depend on {} others {}...".format(d, len(dependencies[d]), dependencies[d][:20]))

trad={}
opeSorted=copy.copy(ope)
for o in opeSorted:
    if o[0]>o[2]:
        o[0],o[2]=o[2],o[0]
    if(o[0][0]=="x" and o[2][0]=="y" and o[0][1:]==o[2][1:] and o[1]=="XOR"):
        trad[o[3]]="XYx"+o[0][1:]
    if(o[0][0]=="x" and o[2][0]=="y" and o[0][1:]==o[2][1:] and o[1]=="AND"):
        trad[o[3]]="XYa"+o[0][1:]
    # print("{} {} {} -> {}".format(o[0],o[1],o[2],o[3]))
for o in opeSorted:
    trado0=o[0]
    trado2=o[2]
    trado3=o[3]
    if o[0] in trad:
        o[0]=trad[o[0]]
    if o[2] in trad:
        o[2]=trad[o[2]]
    if o[3] in trad:
        o[3]=trad[o[3]]
    if o[0]>o[2]:
        o[0],o[2]=o[2],o[0]
    print("{} {} {} -> {}".format(o[0],o[1],o[2],o[3]))

# PART ONE
print("xValue = {}".format(xValue))
print("yValue = {}".format(yValue))
print("actual zValue = {}".format(count))
print("expect zValue = {}".format(xValue+yValue))

print("PART ONE : count = {}".format(count))
# ???

# PART TWO
print("PART TWO : count2 = {}".format(count2))
allpermut=[]
for p in permut:
    allpermut.append(p[0])
    allpermut.append(p[1])
allpermut.sort()
print("PART TWO : res = {}".format(','.join(allpermut)))
# hqh,mmk,pvb,qdq,qvm,vkq,z11,z24,z38,z39   KO


endTime=time.time()
print("Process time spent : {}s".format(round(endTime-startTime,2)))
