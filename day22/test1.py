import re
import copy
import time
import math

# import sys
# sys.setrecursionlimit(15000)

startTime=time.time()

file1 = open('./2024/day22/testpyfile2.csv', 'r')
Lines = file1.readlines()

buyers=[]
for l, line in enumerate(Lines):
    line=line.strip()
    # print(line)
    # allNumbers = re.findall(r'\d+', line)
    # allNumbers=[int(x) for x in allNumbers]
    buyers.append(int(line))

def mix(a,b):
    # print("{}^{}={}".format(a,b,a^b))
    return a^b

def prune(a):
    return a%16777216

def nextSecret(a):
    # print("cur secret = {}".format(secret))
    secret=a*64
    secret=mix(secret, a)
    secret=prune(secret)
    # print("cur secret = {}".format(secret))

    stepSecret=secret
    secret=secret//32
    secret=mix(secret, stepSecret)
    secret=prune(secret)
    # print("cur secret = {}".format(secret))

    stepSecret=secret
    secret=secret*2048
    secret=mix(secret, stepSecret)
    secret=prune(secret)
    # print("cur secret = {}".format(secret))

    return secret

# G = [int(row) for row in line]
# G = [[c for c in row] for row in matrice]
# G2 = [[c for c in row] for row in matrice]
# G3 = [[c for c in row] for row in matrice]

# dir=[[0,1],[1,0],[0,-1],[-1,0]]




# PART ONE
count = 0

def nextSecrets(b, iteration):
    for i in range(iteration):
        nextb=nextSecret(b)
        # print("secret {} {} -> {} -> {} -> {}".format(i, b, nextb, nextb%10, nextb%10-b%10))
        b=nextb
    return b

for b in buyers:
    res=nextSecrets(b,2000)
    # print("result after 2000 for buyer {} : {}".format(b,res))
    count+=res


# PART TWO
count2 = 0

def nextSecrets2(b, iteration):
    arrayPrices=[]
    arraySequence=[]
    for i in range(iteration):
        nextb=nextSecret(b)
        # print("secret {} {} -> {} -> {} -> {}".format(i, b, nextb, nextb%10, nextb%10-b%10))
        arrayPrices.append(nextb%10)
        arraySequence.append(nextb%10-b%10)

        b=nextb
    return arrayPrices, arraySequence


pp=[]
ss=[]

for b in buyers:
    p,s=nextSecrets2(b,2000)
    pp.append(p)
    ss.append(s)
    # print("prices    : {}".format(p))
    # print("sequences : {}".format(s))

# on cherche toutes les sequences
# dicoSec=[]
# for sb in range(len(ss)):
#     for s in range(len(ss[sb])-4):
#         if not ss[sb][s:s+4] in dicoSec:
#             dicoSec.append(ss[sb][s:s+4])
# print("nb total sequence : {}".format(len(dicoSec)))

seqSearch=[-2,1,-1,3]
max=0
for a in range(-3,4):
    for b in range(-3,4):
        for c in range(-3,4):
            for d in range(-3,4):
                seqSearch=[a,b,c,d]
                totalwin=0
                for sb in range(len(ss)):
                    for s in range(len(ss[sb])-4):
                        if ss[sb][s:s+4]==seqSearch:
                            # print("found seq at {} with price {}".format(s,pp[sb][s+3]))
                            totalwin+=pp[sb][s+3]
                            break
                if totalwin>max:
                    max=totalwin
                    endTime=time.time()
                    print("new max for sequence {} : win {} (spent time : {}s)".format(seqSearch, max, round(endTime-startTime,2)))
count2=max

# PART ONE
print("PART ONE : count = {}".format(count))
# 13461553007

# PART TWO
print("PART TWO : count2 = {}".format(count2))
# new max for sequence [0, 2, -2, 2] : win 1499 (spent time : 450.22s) OK


# bSym 4760 for iteration 7860

endTime=time.time()
print("Process time spent : {}s".format(round(endTime-startTime,2)))
