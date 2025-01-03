import re
import copy

file1 = open('./2024/day04/testpyfile2.csv', 'r')
Lines = file1.readlines()

# def func(param):
#     return False
    
matrice=[]
for line in Lines:
    line=line.strip()
    matrice.append(line)

# matrice de caractères
G = [[c for c in row] for row in matrice]
# print(G)
0
# PART ONE
count=0
search="XMAS"
dir=[[1,0],[-1,0],[0,1],[0,-1],[1,1],[1,-1],[-1,1],[-1,-1]]

for l in range(len(G)):
    for c in range(len(G[0])):
        for d in range(len(dir)):
            found=True
            for car in range(len(search)):
                if(0<=l+dir[d][0]*car<len(G) and 0<=c+dir[d][1]*car<len(G[0])):
                    if(G[l+dir[d][0]*car][c+dir[d][1]*car]==search[car]):
                        continue
                    else:
                        found=False
                        break
                else:
                    found=False
                    break
            if found==True:
                count+=1


print("PART ONE : count = {}".format(count))
# 2618

# PART TWO
count2=0
matsearch=["M.S",
           ".A.",
           "M.S"]

def rotateMatrice(matrice):
    rotatedMat=[['' for i in range(len(matrice))] for j in range(len(matrice[0]))]
    for l in range(len(matrice)):
        for c in range(len(matrice[0])):
            rotatedMat[c][len(matrice)-1-l]=matrice[l][c]
    return rotatedMat

matRot=[]
tempMat=[[matsearch[i][j] for i in range(len(matsearch))] for j in range(len(matsearch[0]))]
for i in range(4):
    matRot.append(tempMat)
    tempMat=rotateMatrice(tempMat)
# print(matRot)

for l in range(len(G)-len(matsearch)+1):
    for c in range(len(G[0])-len(matsearch[0])+1):
        for d in range(len(matRot)):
            found=True
            for carl in range(len(matRot[d])):
                for carc in range(len(matRot[d][0])):
                    if(matRot[d][carl][carc]=="." or G[l+carl][c+carc]==matRot[d][carl][carc]):
                        continue
                    else:
                        found=False
                        break
            if found==True:
                count2+=1


print("PART TWO : count2 = {}".format(count2))
