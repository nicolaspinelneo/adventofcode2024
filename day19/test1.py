import re
import copy
import time
import math

import sys
sys.setrecursionlimit(15000)

startTime=time.time()

file1 = open('./2024/day19/testpyfile2.csv', 'r')
Lines = file1.readlines()

# matrice=[]
towels=[]
todsp=[]

for l, line in enumerate(Lines):
    line=line.strip()
    print(line)
    if(l==0):
        towels=line.replace(' ','').split(',')
    elif(l>1):
        todsp.append(line)
    allNumbers = re.findall(r'\d+', line)
    allNumbers=[int(x) for x in allNumbers]
    # matrice.append(line)
print(towels)
print(todsp)


    # allNumbers = re.findall(r'\d+', line)
    # allNumbers=[int(x) for x in allNumbers]
# G = [int(row) for row in line]
# G = [[c for c in row] for row in matrice]
# G2 = [[c for c in row] for row in matrice]
# G3 = [[c for c in row] for row in matrice]

# PART ONE
count = 0
# for t in todsp:
#     tow=copy.copy(towels)
#     curt=t
#     over=False
#     while(len(curt)>0 and len(tow)>0 and not over):
#         # search first pattern
#         found=False
#         for i in range(len(tow)):
#             if(curt[:len(tow[i])]==tow[i]):
#                 print("first of {} are {}".format(t,curt[:len(tow[i])]))
#                 found=True
#                 break
#         if(found==True):
#             curt=curt[len(tow[i]):]
#             tow.pop(i)
#         else:
#             print("{} is not possible".format(t))
#             over=True

#     if(len(curt)==0):
#         print("{} is possible".format(t))
#         count+=1

remainLen=10**9


def isPossible(pat,towels,depth):

    global remainLen
    if remainLen>len(pat):
        remainLen=len(pat)
    # print(depth, len(pat))
    if(len(pat)==0):
        return True
    found=False
    # print("cur tow : {}".format(pat))
    nbMul=0
    for i,t in enumerate(towels):
        if(pat[:len(t)]==t):
            # print("first of {} are {}".format(t,pat[:len(t)]))
            newtowels=copy.copy(towels)
            # newtowels.pop(i)
            # print("found pattern {}".format(t))
            # return isPossible(pat[len(t):], newtowels)
            if(nbMul<1):
                if (isPossible(pat[len(t):], newtowels, depth+1)):
                    nbMul+=1
                    found=True
    # print("nb try above : {}".format(nbMul))
    return found

seen={}
def isPossibleN(pat,towels,depth):
    global seen
    if pat in seen:
        return seen[pat]
    global remainLen
    if remainLen>len(pat):
        remainLen=len(pat)
    # print(depth, len(pat))
    if(len(pat)==0):
        return 1
    found=False
    # print("cur tow : {}".format(pat))
    nbMul=0
    nbFound=0
    for i,t in enumerate(towels):
        if(pat[:len(t)]==t):
            # print("first of {} are {}".format(t,pat[:len(t)]))
            newtowels=copy.copy(towels)
            # newtowels.pop(i)
            # print("found pattern {}".format(t))
            # return isPossible(pat[len(t):], newtowels)
            # if(nbMul<2):
            if(True):
                n=isPossibleN(pat[len(t):], newtowels, depth+1)
                if (n>0):
                    nbMul+=1
                    nbFound+=n
    # print("nb try above : {}".format(nbMul))
    seen[pat]=nbFound
    return nbFound

# for t in todsp:
#     isOk=isPossible(t,towels,0)
#     if isOk:
#         print("{} is possible".format(t))
#         count+=1
#     else:
#         print("{} isnot possible".format(t))

# PART TWO
count2 = 0
for t in todsp:
    nbOk=isPossibleN(t,towels,0)
    if nbOk:
        print("{} is possible with {} sol".format(t,nbOk))
        count2+=nbOk
    else:
        print("{} isnot possible".format(t))

# PART ONE
print("PART ONE : count = {}".format(count))
# ???

# PART TWO
print("PART TWO : count2 = {}".format(count2))
# ???


# bSym 4760 for iteration 7860

endTime=time.time()
print("Process time spent : {}s".format(round(endTime-startTime,2)))
