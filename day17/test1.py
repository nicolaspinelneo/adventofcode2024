import re
import copy
import time
import math

# import sys

# sys.setrecursionlimit(15000)

startTime=time.time()

file1 = open('./2024/day17/testpyfile5.csv', 'r')
Lines = file1.readlines()

matrice=[]
reg=[]
prg=[]
isReg=True
for line in Lines:
    line=line.strip()
    print(line)
    matrice.append(line)
    if(isReg==True and line==""):
        isReg=False
    else:
        allNumbers = re.findall(r'\d+', line)
        if isReg:
            reg.append(int(allNumbers[0]))
        else:
            prg=[int(i) for i in allNumbers]

    # allNumbers = re.findall(r'\d+', line)
    # allNumbers=[int(x) for x in allNumbers]
# G = [int(row) for row in line]
# G = [[c for c in row] for row in matrice]
# G2 = [[c for c in row] for row in matrice]
# G3 = [[c for c in row] for row in matrice]

print("REGS = {}".format(reg))
print("PRGS = {}".format(prg))

def xor(a,b):
    res=0
    # aa=a
    # bb=b
    mul=1
    while(a>0 or b>0):
        res+=mul*(bool(a%2) ^ bool(b%2))
        mul*=2
        a=a//2
        b=b//2
    # print("xor({}, {}) = {}".format(aa,bb,res))
    return res

pnt=0
s=""
while(pnt<len(prg)):
    operande=prg[pnt+1]
    cmb=0
    if operande<4:
        cmb=operande
    elif operande<7:
        cmb=reg[operande-4]
    else:
        print("NOT A VALID PROGRAM !")
        
    # print("cur instr = id : {} inst : {} opeLit = {} opeCmb : {}".format(pnt, prg[pnt], operande, cmb))

    jump=False
    match prg[pnt]:
        case 0:
            res=(reg[0]//(2**cmb))
            reg[0]=res
            # print("intr 0 : put {} / 2**{} on A : {}".format(reg[0], cmb, res))
        case 1:
            res=xor(reg[1], operande)
            reg[1]=res
            # print("intr 1 : put {} XOR {} on B : {}".format(reg[1], operande, res))
        case 2:
            res=cmb%8
            reg[1]=res
            # print("intr 2 : put {} % {} on B : {}".format(cmb, 8, res))
        case 3:
            print("State before jump again {}".format(reg))
            if reg[0]!=0:
                pnt=operande
                jump=True
                # print("intr 3 : jump to {}".format(operande))
        case 4:
            res=xor(reg[1], reg[2])
            # print("intr 4 : put {} XOR {} on B : {}".format(reg[1], reg[2], res))
            reg[1]=res
        case 5:
            res=cmb%8
            s+=str(res)+","
            # print("intr 5 : put {} % {} on output : {}".format(cmb, 8, res))
        case 6:
            res=(reg[0]//(2**cmb))
            reg[1]=res
            # print("intr 6 : put {} / 2**{} on B : {}".format(reg[0], cmb, res))
        case 7:
            res=(reg[0]//(2**cmb))
            reg[2]=res
            # print("intr 7 : put {} / 2**{} on C : {}".format(reg[0], cmb, res))

    # print("res = {}".format(res))
    if not jump:
        pnt+=2

print("REGS = {}".format(reg))
print("PRGS = {}".format(prg))
print("generated string = {}".format(s))
# ==>int(math.floor(729/(2^0)))

# PART ONE
count = 0
if(len(s.replace(",",""))>0):
    count=int(s.replace(",",""))

# PART TWO
count2 = 0

# PART ONE
print("PART ONE : count = {}".format(count))
# KO 433321405
# KO 167430506
# 1,6,7,4,3,0,5,0,6

# PART TWO
print("PART TWO : count2 = {}".format(count2))
# ???


# bSym 4760 for iteration 7860

endTime=time.time()
print("Process time spent : {}s".format(round(endTime-startTime,2)))