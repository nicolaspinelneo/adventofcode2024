import re
import copy

file1 = open('./2024/day02/testpyfile2.csv', 'r')
Lines = file1.readlines()

def isSafe(seq):
    dif=[]
    for i in range(1,len(seq)):
        dif.append(seq[i-1]-seq[i])
    if(dif[0]<0):
        dif=[-x for x in dif]
    print("dif = {}".format(dif))
    if(min(dif)>=1 and (max(dif)<=3)):
        return True
    else:
        return False
    
checkAgain=[]
nbSafe=0
for line in Lines:
    line=line.strip()
    allNumbers = re.findall(r'\d+', line)
    allNumbers=[int(x) for x in allNumbers]
    print(allNumbers)
    if(isSafe(allNumbers)):
        nbSafe+=1
    else:
        checkAgain.append(allNumbers)

print("NEW SEQ TO CHECK")
nbSafe2=0
for allNumbers in checkAgain:
    for eltToRem in range(0, len(allNumbers)):
        allNumbersWithRem=copy.copy(allNumbers)
        allNumbersWithRem.pop(eltToRem)
        print(allNumbersWithRem)
        if(isSafe(allNumbersWithRem)):
            nbSafe2+=1
            break

# PART ONE
# 585
print("nbSafe = {}".format(nbSafe))

# PART TWO
# 626
print("nbSafe2 = {}".format(nbSafe2))
print("nbSafe+nbSafe2 = {}".format(nbSafe+nbSafe2))
