import re
import copy
import time
import math


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
Gscore = [[[-1,-1] for c in row] for row in matrice]
# G3 = [[c for c in row] for row in matrice]

# print(G)
# print(Gdir)

# for l in range(len(G)):
#     print(''.join(G[l]))

pos=[len(G)-2,1]
end=[1,len(G[0])-2]
Gscore[pos[0]][pos[1]]=[0, [0,1]]
dir=[[0,1],[1,0],[0,-1],[-1,0]]

curMinScore=10**9

listHeadPath=[pos]

# PART ONE
count = 0

minScore=10**9

def display():
    for l in range(len(Gscore)):
        s=""
        for c in range(len(Gscore[0])):
            if(Gscore[l][c][0]==-1):
                s+="   "
            else:
                s+=str((Gscore[l][c][0]//1000)%10)+str(Gscore[l][c][0]%10)
                if Gscore[l][c][1]==[1,0]:
                    s+="v"
                elif Gscore[l][c][1]==[-1,0]:
                    s+="^"
                elif Gscore[l][c][1]==[0,1]:
                    s+=">"
                elif Gscore[l][c][1]==[0,-1]:
                    s+="<"
        print(s)

foundShorter=False
while(not foundShorter):
    nextlistHeadPath=[]
    for h in listHeadPath:
        for d in dir:
            if G[h[0]+d[0]][h[1]+d[1]] in [".", "E"]:
                # toAdd=1
                toAdd=1
                sameDir=(Gscore[h[0]][h[1]][1]==d)
                if not sameDir:
                    # toAdd+=1000
                    toAdd+=1000
                if G[h[0]+d[0]][h[1]+d[1]]=="E":
                    # foundShorter=True
                    Gscore[h[0]+d[0]][h[1]+d[1]]=[Gscore[h[0]][h[1]][0]+toAdd,d]
                    print("score : {}".format(Gscore[h[0]][h[1]][0]+toAdd))
                    minScore = min(minScore, Gscore[h[0]][h[1]][0]+toAdd)
                    # display()
                else:
                    if Gscore[h[0]+d[0]][h[1]+d[1]][0]==-1:
                        Gscore[h[0]+d[0]][h[1]+d[1]]=[Gscore[h[0]][h[1]][0]+toAdd,d]
                        nextlistHeadPath.append([h[0]+d[0],h[1]+d[1]])
                    else:
                        if(Gscore[h[0]][h[1]][0]+toAdd<Gscore[h[0]+d[0]][h[1]+d[1]][0]):
                            Gscore[h[0]+d[0]][h[1]+d[1]]=[Gscore[h[0]][h[1]][0]+toAdd,d]
                            nextlistHeadPath.append([h[0]+d[0],h[1]+d[1]])
    listHeadPath=copy.copy(nextlistHeadPath)
    if len(nextlistHeadPath)==0:
        foundShorter=True

count=minScore

display()

# PART TWO
count2 = 0

listHeadPath=[end]
G[end[0]][end[1]]="O"
count2+=1
foundShorter=False
while(not foundShorter):
    nextlistHeadPath=[]
    for h in listHeadPath:
        # minScore=10**9
        # for d in dir:
            # print("Gscore[h[0]+d[0]][h[1]+d[1]][0] : {}".format(Gscore[h[0]+d[0]][h[1]+d[1]][0]))
            # print("Gscore[h[0]][h[1]][0] : {}".format(Gscore[h[0]][h[1]][0]))
            # print("Gscore[h[0]][h[1]][0]-Gscore[h[0]+d[0]][h[1]+d[1]][0] : {}".format(Gscore[h[0]][h[1]][0]-Gscore[h[0]+d[0]][h[1]+d[1]][0]))
            # print("minScore : {}".format(minScore))
            # if Gscore[h[0]+d[0]][h[1]+d[1]][0]!=-1 and Gscore[h[0]][h[1]][0]>Gscore[h[0]+d[0]][h[1]+d[1]][0] and Gscore[h[0]][h[1]][0]-Gscore[h[0]+d[0]][h[1]+d[1]][0] in [1, 1001, -999] and Gscore[h[0]+d[0]][h[1]+d[1]][0]<minScore:
            # if Gscore[h[0]+d[0]][h[1]+d[1]][0]!=-1 and Gscore[h[0]][h[1]][0]-Gscore[h[0]+d[0]][h[1]+d[1]][0] in [1, 1001, -999] and Gscore[h[0]+d[0]][h[1]+d[1]][0]<minScore:
            # if Gscore[h[0]+d[0]][h[1]+d[1]][0]!=-1 and Gscore[h[0]][h[1]][0]-Gscore[h[0]+d[0]][h[1]+d[1]][0] in [1, 1001, -999]:
                # minScore=Gscore[h[0]+d[0]][h[1]+d[1]][0]
        for d in dir:
            # if Gscore[h[0]+d[0]][h[1]+d[1]][0]!=-1 and Gscore[h[0]+d[0]][h[1]+d[1]][0]==minScore:
            if Gscore[h[0]+d[0]][h[1]+d[1]][0]!=-1 and G[h[0]+d[0]][h[1]+d[1]]!="O" and Gscore[h[0]][h[1]][0]-Gscore[h[0]+d[0]][h[1]+d[1]][0] in [1, 1001, -999]:
            # if Gscore[h[0]+d[0]][h[1]+d[1]][0]!=-1 and G[h[0]+d[0]][h[1]+d[1]]!="*" and d==[-Gscore[h[0]+d[0]][h[1]+d[1]][1][0],-Gscore[h[0]+d[0]][h[1]+d[1]][1][1]]:
                # for l in range(len(G)):
                #     print(''.join(G[l]))
                # print(Gscore[h[0]+d[0]][h[1]+d[1]][1])
                if(Gscore[h[0]][h[1]][1]!=Gscore[h[0]+d[0]][h[1]+d[1]][1] and G[h[0]-d[0]][h[1]-d[1]]=="O"):
                    G[h[0]+d[0]][h[1]+d[1]]="O"
                    count2+=1
                    nextlistHeadPath.append([h[0]+d[0],h[1]+d[1]])
                if(Gscore[h[0]][h[1]][1]==Gscore[h[0]+d[0]][h[1]+d[1]][1]):
                    G[h[0]+d[0]][h[1]+d[1]]="O"
                    count2+=1
                    nextlistHeadPath.append([h[0]+d[0],h[1]+d[1]])
    listHeadPath=copy.copy(nextlistHeadPath)
    if [h[0],h[1]]==pos or len(listHeadPath)==0:
        foundShorter=True
    # for l in range(len(G)):
    #     print(''.join(G[l]))

for l in range(len(G)):
    print(''.join(G[l]))

# PART ONE
print("PART ONE : count = {}".format(count))
# 99520 not good
# 98520

# PART TWO
print("PART TWO : count2 = {}".format(count2))
# 540 : too low
# 631 : too high


# bSym 4760 for iteration 7860

endTime=time.time()
print("Process time spent : {}s".format(round(endTime-startTime,2)))
