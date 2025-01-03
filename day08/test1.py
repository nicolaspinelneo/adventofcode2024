import re
import copy
import time

startTime=time.time()

file1 = open('./2024/day08/testpyfile2.csv', 'r')
Lines = file1.readlines()


matrice=[]
for line in Lines:
    line=line.strip()
    print(line)
    matrice.append(line)
    # allNumbers = re.findall(r'\d+', line)
    # allNumbers=[int(x) for x in allNumbers]
G = [[c for c in row] for row in matrice]
G2 = [[c for c in row] for row in matrice]
G3 = [[c for c in row] for row in matrice]
print(G)

# PART ONE
count = 0
dic={}
# find every antenna an store coordinates
for l in range(len(G)):
    for c in range(len(G[0])):
        if G[l][c]!=".":
            # dic[G[l][c]].append([l, c])
            if G[l][c] in dic:
                dic[G[l][c]]+=[[l, c]]
            else:
                dic[G[l][c]]=[[l, c]]
print(dic)

for a in dic:
    print("for {}, content {}".format(a, dic[a]))
    for ant1 in range(len(dic[a])-1):
        for ant2 in range(ant1+1, len(dic[a])):
            dif=[dic[a][ant1][0]-dic[a][ant2][0], dic[a][ant1][1]-dic[a][ant2][1]]
            print("difl {} difc {}".format(dif[0], dif[1]))
            antipodes=[[dic[a][ant1][0]+dif[0], dic[a][ant1][1]+dif[1]],[dic[a][ant2][0]-dif[0], dic[a][ant2][1]-dif[1]]]
            print("antipode1 {} antipode2 {}".format(antipodes[0], antipodes[1]))
            for a2 in range(len(antipodes)):
                # if(0<=antipodes[a2][0]<len(G) and 0<=antipodes[a2][1]<len(G[0]) and G[antipodes[a2][0]][antipodes[a2][1]]=="."):
                if(0<=antipodes[a2][0]<len(G) and 0<=antipodes[a2][1]<len(G[0]) and G2[antipodes[a2][0]][antipodes[a2][1]]!="#"):
                    G2[antipodes[a2][0]][antipodes[a2][1]]="#"
                    count+=1


for l in range(len(G2)):
    line=""
    for c in range(len(G2[0])):
        line+=G2[l][c]
    print(line)

# PART TWO
count2 = 0
for a in dic:
    print("for {}, content {}".format(a, dic[a]))
    for ant1 in range(len(dic[a])-1):
        for ant2 in range(ant1+1, len(dic[a])):
            dif=[dic[a][ant1][0]-dic[a][ant2][0], dic[a][ant1][1]-dic[a][ant2][1]]
            print("difl {} difc {}".format(dif[0], dif[1]))

            curAntipode=[dic[a][ant1][0], dic[a][ant1][1]]
            antipodes=[]
            while(0<=curAntipode[0]<len(G) and 0<=curAntipode[1]<len(G[0])):
                antipodes.append(curAntipode)
                if(G3[curAntipode[0]][curAntipode[1]]!="#"):
                    G3[curAntipode[0]][curAntipode[1]]="#"
                    count2+=1
                curAntipode=[curAntipode[0]+dif[0],curAntipode[1]+dif[1]]
            
            curAntipode=[dic[a][ant1][0]-dif[0], dic[a][ant1][1]-dif[1]]
            antipodes=[]
            while(0<=curAntipode[0]<len(G) and 0<=curAntipode[1]<len(G[0])):
                antipodes.append(curAntipode)
                if(G3[curAntipode[0]][curAntipode[1]]!="#"):
                    G3[curAntipode[0]][curAntipode[1]]="#"
                    count2+=1
                curAntipode=[curAntipode[0]-dif[0],curAntipode[1]-dif[1]]


    
# PART ONE
print("PART ONE : count = {}".format(count))
# KO 387
# KO 354
376


# PART TWO
print("PART TWO : count2 = {}".format(count2))
# ???

endTime=time.time()
print("Process time spent : {}s".format(round(endTime-startTime,2)))
