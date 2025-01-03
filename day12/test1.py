import re
import copy
import time

startTime=time.time()

file1 = open('./2024/day12/testpyfile.csv', 'r')
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
# G2 = [[c for c in row] for row in matrice]
# G3 = [[c for c in row] for row in matrice]
print(G)

dir=[[0,1],[1,0],[0,-1],[-1,0]]

def markFirstZone(l, c, t, dd):
    if(not (0<=l<len(G) and 0<=c<len(G[0]))):
        return
    if([l, c] in seen):
        return
    if(t!=G[l][c]):
        return
    # if [l, c] in p:
        # p.remove([l, c])
    for d in range(len(dir)):
        # if((d+2)%4!=dd):
            # if not [l+dir[d][0], c+dir[d][1]] in p:
        p.append([l+dir[d][0], c+dir[d][1]])
    seen.append([l, c])
    for d in range(len(dir)):
        markFirstZone(l+dir[d][0], c+dir[d][1], t, d)
    return

# PART ONE
count = 0

for l in range(len(G)):
    for c in range(len(G[0])):
        if(G[l][c]!="."):
            seen=[]
            p=[]
            markFirstZone(l,c,G[l][c],-1)
            for pp in range(len(p)-1,-1,-1):
                if p[pp] in seen:
                    p.remove(p[pp])
            print("zone {} area = {}, perim= {} = {} \ {}".format(G[l][c], len(seen), len(p), seen, p))
            count+=len(seen)*len(p)
            for z in range(len(seen)):
                G[seen[z][0]][seen[z][1]]="."


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
