import re
import copy
import time
import math

# import sys
# sys.setrecursionlimit(15000)

startTime=time.time()

test=False

if test:
    file1 = open('./2024/day20/testpyfile1.csv', 'r')
else:
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

# nbcheat={}
# for l in range((len(Gt))):
#     for c in range(len(Gt[0])):
#         if(Gt[l][c]==-1 and 0<l<len(Gt)-1 and 0<c<len(Gt[0])-1):
#             cheat=-1
#             if(Gt[l+dir[0][0]][c+dir[0][1]]>=0 and Gt[l+dir[2][0]][c+dir[2][1]]>=0):
#                 cheat=abs(Gt[l+dir[0][0]][c+dir[0][1]]-Gt[l+dir[2][0]][c+dir[2][1]])-2
#             if(Gt[l+dir[1][0]][c+dir[1][1]]>=0 and Gt[l+dir[3][0]][c+dir[3][1]]>=0):
#                 cheat=abs(Gt[l+dir[1][0]][c+dir[1][1]]-Gt[l+dir[3][0]][c+dir[3][1]])-2
#             if(cheat>=0):
#                 if(cheat>=100):
#                     count+=1
#                     if(cheat in nbcheat):
#                         nbcheat[cheat]+=1
#                     else:
#                         nbcheat[cheat]=1

# print(nbcheat)

# PART TWO
count2 = 0

nbcheat={}
# for l in range((len(Gt))):
#     for c in range(len(Gt[0])):
#         if(Gt[l][c]==-1 and 0<l<len(Gt)-1 and 0<c<len(Gt[0])-1):
#             # pour chaque mur, si 1 case adjacente est . (Gt[][]>=0), alors on cherche toutes les sorties possible de ce groupe de mur
#             cheat=-1
#             if(Gt[l+dir[0][0]][c+dir[0][1]]>=0 and Gt[l+dir[2][0]][c+dir[2][1]]>=0):
#                 cheat=abs(Gt[l+dir[0][0]][c+dir[0][1]]-Gt[l+dir[2][0]][c+dir[2][1]])-2
#             if(Gt[l+dir[1][0]][c+dir[1][1]]>=0 and Gt[l+dir[3][0]][c+dir[3][1]]>=0):
#                 cheat=abs(Gt[l+dir[1][0]][c+dir[1][1]]-Gt[l+dir[3][0]][c+dir[3][1]])-2
#             if(cheat>=0):
#                 if test:
#                     if(cheat>=50):
#                         # count2+=1
#                         if(cheat in nbcheat):
#                             nbcheat[cheat]+=1
#                         else:
#                             nbcheat[cheat]=1
#                 else:
#                     if(cheat>=100):
#                         # count2+=1
#                         if(cheat in nbcheat):
#                             nbcheat[cheat]+=1
#                         else:
#                             nbcheat[cheat]=1

# print(nbcheat)

# for l in range(len(Gt)):
#     s=""
#     for c in range(len(Gt[0])):
#         s+=str(Gt[l][c])+";"
#     print(s)

dicrac={}
for lc in range(len(Gt)*len(Gt[0])-1):
    l=lc//len(Gt[0])
    c=lc%len(Gt[0])
    for llcc in range(lc+1,min(len(Gt)*len(Gt[0]),lc+1+20+20*len(Gt[0]))):
        ll=llcc//len(Gt[0])
        cc=llcc%len(Gt[0])
        if(Gt[l][c]>=0 and Gt[ll][cc]>=0):
            rac=abs(Gt[l][c]-Gt[ll][cc])-(abs(l-ll)+abs(c-cc))
            if(test):
                if((abs(l-ll)+abs(c-cc))<=20 and rac>=50):
                    if rac in dicrac:
                        dicrac[rac]+=1
                    else:
                        dicrac[rac]=1
                    if(rac==72):
                        # print("rac {} for s=[{},{}] e=[{},{}]".format(rac,l,c,ll,cc))
                        zz=0
                    count2+=1
            else:
                if((abs(l-ll)+abs(c-cc))<=20 and rac>=100):
                    if rac in dicrac:
                        dicrac[rac]+=1
                    else:
                        dicrac[rac]=1
                    count2+=1

nbcheatSorted= list(dicrac.keys())
nbcheatSorted.sort()
sorted={i: dicrac[i] for i in nbcheatSorted}

# for n in sorted:
#     print("There are {} cheats that save {} picoseconds.".format(sorted[n], n))

print("PART TWO : count2 = {}".format(count2))

Gred=[["." for c in row] for row in matrice]
for l in range(1,len(G)-1):
    for c in range(1,len(G[0])-1):
        onlyWalls=True
        for d in dir:
            if G[l+d[0]][c+d[1]]!="#":
                # not a wall
                onlyWalls=False
                break
        if onlyWalls==True:
            Gred[l][c]="#"

# for x in range(0,1000):
# spread reduction zone once
for l in range(1,len(G)-1):
    for c in range(1,len(G[0])-1):
        if Gred[l][c]=="#":
            for d in dir:
                if G[l+d[0]][c+d[1]]=="#":
                    Gred[l+d[0]][c+d[1]]="#"

arrayPos=[]
for l in range(1,len(G)-1):
    for c in range(1,len(G[0])-1):
        if Gred[l][c]=="#":
            for d in dir:
                if Gred[l+d[0]][c+d[1]]=="." and Gt[l+d[0]][c+d[1]]>=0:
                    if not [l+d[0],c+d[1]] in arrayPos:
                        arrayPos.append([l+d[0],c+d[1]])

# print(arrayPos)

# for i in range(len(arrayPos))

# for l in range(len(Gred)):
#     print(''.join(Gred[l]))


def updateZone(pos,z):
    if not (0<=pos[0]<len(G) and 0<=pos[1]<len(G[0])):
        return
    if Gred[pos[0]][pos[1]]!="#":
        return
    if Gredz[pos[0]][pos[1]]!=0:
        return
    Gredz[pos[0]][pos[1]]=z
    for d in dir:
        updateZone([pos[0]+d[0],pos[1]+d[1]],z)
    
# find zones
zone=1
Gredz=[[0 for c in row] for row in matrice]
for l in range(1,len(G)-1):
    for c in range(1,len(G[0])-1):
        if Gred[l][c]=="#" and Gredz[l][c]==0:
            # new zone to mark
            updateZone([l,c],zone)
            zone+=1

arroundZones={}
for l in range(1,len(G)-1):
    for c in range(1,len(G[0])-1):
        if Gredz[l][c]>0:
            for d in dir:
                if G[l+d[0]][c+d[1]]!="#":
                    if str(Gredz[l][c]) in arroundZones:
                        if not [l+d[0],c+d[1]] in arroundZones[str(Gredz[l][c])]:
                            arroundZones[str(Gredz[l][c])].append([l+d[0],c+d[1]])
                    else:
                        arroundZones[str(Gredz[l][c])]=[[l+d[0],c+d[1]]]

# print(arroundZones)

# print("_"*30)
# for l in range(len(Gredz)):
#     s=""
#     for c in range(len(Gredz[0])):
#         if Gredz[l][c]==0:
#             s+="."
#         else:
#             s+=str((Gredz[l][c]%10))
#     print(s)

for z in arroundZones:
    # print("zone {} = {}".format(z, arroundZones[z]))
    for s in range(len(arroundZones[z])-1):
        for e in range(s+1, len(arroundZones[z])):
            ss=arroundZones[z][s]
            ee=arroundZones[z][e]
            if abs(ss[0]-ee[0])+abs(ss[1]-ee[1])>2 and abs(ss[0]-ee[0])+abs(ss[1]-ee[1])<=20:
            # if abs(ss[0]-ee[0])+abs(ss[1]-ee[1])>=0 and abs(ss[0]-ee[0])+abs(ss[1]-ee[1])<=2000:
                cheat=abs(Gt[ss[0]][ss[1]]-Gt[ee[0]][ee[1]])-(abs(ss[0]-ee[0])+abs(ss[1]-ee[1]))
                if test:
                    if cheat>=50:
                        if cheat==72:
                            # print("ss = {}".format(ss))
                            # print("ee = {}".format(ee))
                            # print("rac {} for s=[{},{}] e=[{},{}]".format(cheat,ss[0],ss[1],ee[0],ee[1]))
                            zz=0
                        # count2+=1
                        if(cheat in nbcheat):
                            nbcheat[cheat]+=1
                        else:
                            nbcheat[cheat]=1
                else:
                    if cheat>=100:
                        # count2+=1
                        if(cheat in nbcheat):
                            nbcheat[cheat]+=1
                        else:
                            nbcheat[cheat]=1

# nbcheatSorted= list(nbcheat.keys())
# nbcheatSorted.sort()
# sorted={i: nbcheat[i] for i in nbcheatSorted}

# for n in sorted:
#     print("There are {} cheats that save {} picoseconds.".format(sorted[n], n))



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
# 121533 KO
# 92616 KO
# 43455093 KO
# 1015092


# bSym 4760 for iteration 7860

endTime=time.time()
print("Process time spent : {}s".format(round(endTime-startTime,2)))
