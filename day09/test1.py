import re
import copy
import time

startTime=time.time()

file1 = open('./2024/day09/testpyfile.csv', 'r')
Lines = file1.readlines()


# matrice=[]
for line in Lines:
    line=line.strip()
    print(line)
    # matrice.append(line)
    # allNumbers = re.findall(r'\d+', line)
    # allNumbers=[int(x) for x in allNumbers]
G = [int(row) for row in line]
# G = [[c for c in row] for row in matrice]
# G2 = [[c for c in row] for row in matrice]
# G3 = [[c for c in row] for row in matrice]
# print(G)

# PART ONE
count = 0
file=True
disk=[]
idFile=0
nbEmpty=0
for i in range(len(G)):
    if(file==True):
        for j in range(G[i]):
            disk.append(idFile)
        idFile+=1
    else:
        for j in range(G[i]):
            disk.append(-1)
        nbEmpty+=G[i]
    file=not file
print("")
print("PARTITIONNED DISK :")
# print(disk)

posEndDisk=len(disk)-1
posEmpty=0
idCount=0
i=0
# for i in range(0, nbEmpty):
while(posEmpty<posEndDisk-1):
    while(disk[posEmpty]!=-1):
       count+=(idCount*int(disk[posEmpty]))
    #    print("{} * {}".format(idCount, int(disk[posEmpty])))
       idCount+=1
       posEmpty+=1
    disk[posEmpty]=disk[posEndDisk]
    # print(disk[posEmpty])
    # print("{} * {}".format(idCount, int(disk[posEmpty])))
    # count+=(idCount*int(disk[posEmpty]))
    # idCount+=1
    disk[posEndDisk]=-1
    while(disk[posEndDisk]==-1):
        posEndDisk-=1
    logLine=""
    # for j in range(len(disk)):
    #     logLine+=disk[j]
    # print(logLine)
    i+=1

while(disk[posEmpty]!=-1):
    count+=(idCount*int(disk[posEmpty]))
#    print("{} * {}".format(idCount, int(disk[posEmpty])))
    idCount+=1
    posEmpty+=1

for j in range(len(disk)):
    logLine+=str(disk[j])
print("")
print("UNPARTITIONNED DISK :")
print(logLine)

# PART TWO
count2 = 0

# PART ONE
print("PART ONE : count = {}".format(count))
# KO 89314291449
# KO 89312744865
# 6283170117911


# PART TWO
print("PART TWO : count2 = {}".format(count2))
# ???

endTime=time.time()
print("Process time spent : {}s".format(round(endTime-startTime,2)))
