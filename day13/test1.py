import re
import copy
import time
import math

startTime=time.time()

file1 = open('./2024/day13/testpyfile2.csv', 'r')
Lines = file1.readlines()

# matrice=[]
machine=[]
nbMachine=0
for l, line in enumerate(Lines):
    line=line.strip()
    # print(line)
    # matrice.append(line)
    allNumbers = re.findall(r'\d+', line)
    allNumbers=[int(x) for x in allNumbers]
    if(l%4==0):
        # button A
        machine.append([])
        nbMachine+=1
        machine[nbMachine-1].append(allNumbers)
    elif(l%4==1):
        # button B
        machine[nbMachine-1].append(allNumbers)
    elif(l%4==2):
        # prize
        machine[nbMachine-1].append(allNumbers)
# G = [int(row) for row in line]
# G = [[c for c in row] for row in matrice]
# G2 = [[c for c in row] for row in matrice]
# G3 = [[c for c in row] for row in matrice]
# print(machine)

# PART ONE
count = 0
for m in range(len(machine)):
    # print("nb A for X : {}/{}={} ; nb A for Y : {}/{}={} ; ".format(machine[m][2][0], machine[m][0][0], machine[m][2][0]//machine[m][0][0], machine[m][2][1], machine[m][0][1], machine[m][2][1]//machine[m][0][1]))
    # print("nb B for X : {}/{}={} ; nb B for Y : {}/{}={} ; ".format(machine[m][2][0], machine[m][1][0], machine[m][2][0]//machine[m][1][0], machine[m][2][1], machine[m][1][1], machine[m][2][1]//machine[m][1][1]))
    # print("")

    found=False
    for a in range(100):
        for b in range(100):
            if(machine[m][0][0]*a+machine[m][1][0]*b==machine[m][2][0] and machine[m][0][1]*a+machine[m][1][1]*b==machine[m][2][1]):
                # print("found : nbA={}, nbB={}".format(a,b))
                found=True
                break
        if found==True:
            break
    if found==True:
        count+=a*3+b

# PART TWO
count2 = 0

for m in range(len(machine)):
    machine[m][2][1]+=10000000000000
    machine[m][2][0]+=10000000000000
    # print("nb A for X : {}/{}={} ; nb A for Y : {}/{}={} ; ".format(machine[m][2][0], machine[m][0][0], machine[m][2][0]//machine[m][0][0], machine[m][2][1], machine[m][0][1], machine[m][2][1]//machine[m][0][1]))
    # print("nb B for X : {}/{}={} ; nb B for Y : {}/{}={} ; ".format(machine[m][2][0], machine[m][1][0], machine[m][2][0]//machine[m][1][0], machine[m][2][1], machine[m][1][1], machine[m][2][1]//machine[m][1][1]))

    ax, ay=machine[m][0]
    bx, by=machine[m][1]
    px, py=machine[m][2]
    # cnb=(machine[m][2][0]-machine[m][2][1]*machine[m][0][0]/machine[m][0][1])/(machine[m][1][0]-machine[m][1][1]*machine[m][0][0]/machine[m][0][1])
    # cna=(machine[m][2][0]-machine[m][1][0]*cnb)/machine[m][0][0]
    cnb=(ax*py-ay*px)/(ax*by-ay*bx)
    cna=(px-cnb*bx)/ax
    # if(abs(cna-round(cna))<0.001 and abs(cnb-round(cnb))<0.001):
    #     # print("compute cna={} ; cnb={}".format(cna, cnb))
    #     cnai=int(round(cna))
    #     cnbi=int(round(cnb))
    #     count2+=cnai*3+cnbi
    cnai=int(round(cna))
    cnbi=int(round(cnb))
    if(cnai*ax+cnbi*bx==px and cnai*ay+cnbi*by==py):
        # print("compute cna={} ; cnb={}".format(cna, cnb))
        # print("solution cna {}, cnb : {}".format(cna, cnb))
        count2+=cnai*3+cnbi
    # else:
    #     print("no solution difx {}, dify : {}".format(cnai*ax+cnbi*bx-px, cnai*ay+cnbi*by-py))
    # found=False
    # for a in range(100):
    #     for b in range(100):
    #         if(machine[m][0][0]*a+machine[m][1][0]*b==machine[m][2][0] and machine[m][0][1]*a+machine[m][1][1]*b==machine[m][2][1]):
    #             print("found : nbA={}, nbB={}".format(a,b))
    #             found=True
    #             break
    #     if found==True:
    #         break
    # if found==True:
    #     count2+=a*3+b

# PART ONE
print("PART ONE : count = {}".format(count))
# 36758


# PART TWO
print("PART TWO : count2 = {}".format(count2))
# 76358113886726

endTime=time.time()
print("Process time spent : {}s".format(round(endTime-startTime,2)))
