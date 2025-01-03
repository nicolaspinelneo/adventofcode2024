import re
import copy
import time

startTime=time.time()

file1 = open('./2024/day09/testpyfile2.csv', 'r')
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

# PART TWO
count2 = 0
file=True

idfile=[]
isfile=[]
lenfile=[]

id=0
for i in range(len(G)):
    if(file==True):
        idfile.append(id)
        id+=1
    else:
        idfile.append(-1)
    isfile.append(file)
    lenfile.append(G[i])
    file=not file
print("")
print("PARTITIONNED DISK :")
# print(idfile)
# print(isfile)
# print(lenfile)

# 0.1.2.3.4.5.6.7.8.9 idfile
# 1010101010101010101 isfile
# 2333133121414131402 lenfile

# 09
# 11010101010101010101
# 22133133121414131402

def printcheckstr(idfile, isfile, lenfile):
    checkstr=""
    for i in range(len(isfile)):
        if not isfile[i]:
            checkstr+="."*lenfile[i]
        else:
            for j in range(lenfile[i]):
                checkstr+=str(idfile[i]%10)

    # print(checkstr)
    for page in range(0, len(checkstr),11850):
        print(checkstr[page:page+11850])

# printcheckstr(idfile, isfile, lenfile)

for idsrc in range(len(idfile)-1,-1,-1):
    if(isfile[idsrc]==False):
        continue
    iddest=0
    found=False
    while(isfile[iddest]==True or lenfile[iddest]<lenfile[idsrc] and iddest<idsrc):
        iddest+=1
    if(iddest<idsrc):
        # print("found space for file")
        lenfile[iddest]-=lenfile[idsrc]
        # idfile.insert(iddest,idfile.pop(idsrc))
        # isfile.insert(iddest,isfile.pop(idsrc))
        # lenfile.insert(iddest,lenfile.pop(idsrc))
        idfile.insert(iddest,idfile[idsrc])
        isfile.insert(iddest,isfile[idsrc])
        lenfile.insert(iddest,lenfile[idsrc])
        isfile[idsrc+1]=False
        


print("")
print("UNPARTITIONNED DISK :")
# print(idfile)
# print(isfile)
# print(lenfile)

mul=0
for i in range(len(isfile)):
    if not isfile[i]:
        mul+=lenfile[i]
    else:
        for j in range(lenfile[i]):
            count2+=(mul*idfile[i])
            mul+=1

# printcheckstr(idfile, isfile, lenfile)

# PART ONE
print("PART ONE : count = {}".format(count))
# KO 89314291449
# KO 89312744865
# 6283170117911


# PART TWO
print("PART TWO : count2 = {}".format(count2))
# 6307653242596

endTime=time.time()
print("Process time spent : {}s".format(round(endTime-startTime,2)))
