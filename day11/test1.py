import re
import copy
import time

startTime=time.time()

file1 = open('./2024/day11/testpyfile2.csv', 'r')
Lines = file1.readlines()

# matrice=[]
for line in Lines:
    line=line.strip()
    print(line)
    # matrice.append(line)
    allNumbers = re.findall(r'\d+', line)
    allNumbers=[int(x) for x in allNumbers]
# G = [int(row) for row in line]
# G = [[int(c) for c in row] for row in matrice]
# G2 = [[c for c in row] for row in matrice]
# G3 = [[c for c in row] for row in matrice]
print(allNumbers)

# PART ONE
count = 0

def blink(allNumbers):
    newAllNumbers=[]
    for a in range(len(allNumbers)):
        if allNumbers[a]==0:
            newAllNumbers.append(1)
        elif len(str(allNumbers[a]))%2==0:
            lna=len(str(allNumbers[a]))//2
            newAllNumbers.append(int(str(allNumbers[a])[0:lna]))
            newAllNumbers.append(int(str(allNumbers[a])[lna:]))
        else:
            newAllNumbers.append(allNumbers[a]*2024)
    # print(newAllNumbers)
    return newAllNumbers

allNumberstoParse=[x for x in allNumbers]
for b in range(25):
    allNumberstoParse=blink(allNumberstoParse)
    # print(allNumberstoParse)
count=len(allNumberstoParse)

# PART TWO
count2 = 0
allNumberstoParse=[x for x in allNumbers]

seen={}
def recur(nb, depth):
    expectedReturnedValue=-1
    if str(nb)+","+str(depth) in seen:
        return seen[str(nb)+","+str(depth)]
    if depth==0:
        valToReturn=1
        seen[(str(nb)+","+str(depth))]=valToReturn
        return valToReturn
    else:
        if nb==0:
            valToReturn=1
            valToReturn=recur(1,depth-1)
            seen[(str(nb)+","+str(depth))]=valToReturn
            return valToReturn
        elif len(str(nb))%2==0:
            lna=len(str(nb))//2
            valToReturn=recur(int(str(nb)[0:lna]),depth-1)+recur(int(str(nb)[lna:]),depth-1)
            seen[(str(nb)+","+str(depth))]=valToReturn
            return valToReturn
        else:
            valToReturn=recur(nb*2024,depth-1)
            seen[(str(nb)+","+str(depth))]=valToReturn
            return valToReturn

for nb in range(len(allNumberstoParse)):
    count2+=recur(allNumberstoParse[nb],75)

# PART ONE
print("PART ONE : count = {}".format(count))
# 203953


# PART TWO
print("PART TWO : count2 = {}".format(count2))
# 242090118578155

endTime=time.time()
print("Process time spent : {}s".format(round(endTime-startTime,2)))
