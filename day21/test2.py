import re
import copy
import time
import math

import sys
sys.setrecursionlimit(15000)

startTime=time.time()

file1 = open('./2024/day21/testpyfile2.csv', 'r')
Lines = file1.readlines()

codes=[]
dg=[]
for l, line in enumerate(Lines):
    line=line.strip()
    # print(line)
    allNumbers = re.findall(r'\d+', line)
    codes.append(int(allNumbers[0]))
    dg.append([d for d in line])

# depth=0
depth=23
# +---+---+---+
# | 7 | 8 | 9 |
# +---+---+---+  #     +---+---+
# | 4 | 5 | 6 |  #     | ^ | A |
# +---+---+---+  # +---+---+---+
# | 1 | 2 | 3 |  # | < | v | > |
# +---+---+---+  # +---+---+---+
#     | 0 | A |
#     +---+---+

# <v<A>>^A<vA<A>>^AAvAA<^A>A<v<A>>^AAvA^A<vA>^AA<A>A<v<A>A>^AAAvA<^A>A
#    <   A  v <   AA >>  ^ A   <   AA > A  v  AA ^ A   < v  AAA >  ^ A
#        ^        <<       A       ^^   A     >>   A        vvv      A
#                          1            7          9                 A

# <<vAA>A^>A<A>vA^A<vA<A^>>A<A>vAA^A<<vA>>^AAvA^A<vA>^AA<A>A<<vA>A^>AAA<A>vA^A
#    << v  A ^  > A  v <   A ^  >> A   <   AA > A  v  AA ^ A   < v  AAA ^  > A
#          <      ^        <       A       ^^   A     >>   A        vvv      A
#                                  1            7          9                 A

diccombi={}

def recCombi(str):
    if str in diccombi:
        return diccombi[str]
    if(len(str)<2):
        return [str]
    else:
        combi=[]
        for c in range(len(str)):
            rest=""
            if c>0:
                rest+=str[:c]
            if c<len(str)-1:
                rest+=str[c+1:]
            # print("{} and {}".format(str[c],rest))
            subCombi=recCombi(rest)
            for sc in subCombi:
                if(not str[c]+sc in combi):
                    combi.append(str[c]+sc)
        diccombi[str]=combi
        return combi

direc={">":[1,0],
       "<":[-1,0],
       "v":[0,1],
       "^":[0,-1]}
numbers={
    '0':[1,3],
    '1':[0,2],
    '2':[1,2],
    '3':[2,2],
    '4':[0,1],
    '5':[1,1],
    '6':[2,1],
    '7':[0,0],
    '8':[1,0],
    '9':[2,0],
    'A':[2,3]
}
arrows={
    '^':[1,0],
    'A':[2,0],
    '<':[0,1],
    'v':[1,1],
    '>':[2,1]
}

dicoAutCom={}
def getAutCom(comb, curPos):
    # if "{},{}".format(comb,curPos) in dicoAutCom:
    #     return dicoAutCom["{},{}".format(comb,curPos)]
    autorizedComb=[]
    for c in comb:
        curPosCheck=copy.copy(curPos)
        forbidden=False
        for d in c:
            curPosCheck=[curPosCheck[0]+direc[d][0],curPosCheck[1]+direc[d][1]]
            if curPosCheck==[0,3]:
                #forbidden
                forbidden=True
                break
        if not forbidden:
            autorizedComb.append(c)
    comb=copy.copy(autorizedComb)
    return comb

dicoAutCom2={}
def getAutCom2(comb, curPos):
    # if "{},{}".format(comb,curPos) in dicoAutCom2:
    #     return dicoAutCom2["{},{}".format(comb,curPos)]
    autorizedComb=[]
    for c in comb:
        curPosCheck=copy.copy(curPos)
        forbidden=False
        for d in c:
            curPosCheck=[curPosCheck[0]+direc[d][0],curPosCheck[1]+direc[d][1]]
            if curPosCheck==[0,0]:
                #forbidden
                forbidden=True
                break
        if not forbidden:
            autorizedComb.append(c)
    comb=copy.copy(autorizedComb)
    return comb

dicoOptCom={}
def getOptCom(comb):
    if "{}".format(comb) in dicoOptCom:
        return dicoAutCom["{}".format(comb)]
    optimizedComb=[]
    for c in comb:
        nbChange=0
        curDir=-1
        for d in c:
            if curDir==-1:
                curDir=d
            else:
                if curDir!=d:
                    curDir=d
                    nbChange+=1
        if nbChange<2:
            optimizedComb.append(c)
    comb=copy.copy(optimizedComb)
    return comb


seen={}
def getseq(seq, iteration, item):
    global seen
    if "{},{}".format(seq, iteration) in seen:
        return seen["{},{}".format(seq, iteration)]
    if(iteration>2+depth):
        return len(seq)
        # return seq
    if(iteration==0):
        digits=numbers
    else:
        digits=arrows
    curPos=digits["A"] # A
    # print("iter{} from A".format(iteration))
    # nextSeq=""
    nextSeqLen=0
    for se in seq:
        goto=digits[se]
        # print("{}-> it {} : option {} Want to reach {}".format("-"*(iteration*3), iteration, item, se))
        stoadd=""
        for i, dir in enumerate([[">", "<"],["v","^"]]):
            if(curPos[i]<goto[i]):
                stoadd+=dir[0]*abs(curPos[i]-goto[i])
            elif(curPos[i]>goto[i]):
                stoadd+=dir[1]*abs(curPos[i]-goto[i])

        # on cherche toutes les combinaisons
        comb=recCombi(stoadd)
        # comb=[stoadd]

        # check if not forbidden position for each combi
        if iteration==0:
            comb=getAutCom(comb,curPos)

        if(iteration>0):
            comb=getAutCom2(comb,curPos)
            comb=getOptCom(comb)

        comb=[c+"A" for c in comb]

        # print("{}-> it {} : possible options {}".format("-"*(iteration*3), iteration, comb))
        # appel plusieurs fois getSeq sur chaque sous partie, et additionne !
        minSeq=""
        m=-1
        for i, d in enumerate(comb):
            # print(">it {} item {} portion in = {}".format(iteration, item, d))
            # newPortion=getseq(d,iteration+1,i)
            newPortionLen=getseq(d,iteration+1,i)
            # print("<it {} portion out = {}, seq = {}".format(iteration, newPortion, nextSeq))
            if(m==-1):
                # minSeq=newPortion
                # m=len(newPortion)
                m=newPortionLen
                # if(iteration==1):
                #     print("{}-> it {} first min = {}".format("-"*(iteration*3), iteration, m))
            else:
                # if(iteration==1):
                #     print("{}-> it {} new min test = {}".format("-"*(iteration*3), iteration, len(newPortion)))
                # if len(newPortion)<m:
                if newPortionLen<m:
                    # minSeq=newPortion
                    # m=len(newPortion)
                    m=newPortionLen
                    # if(iteration==1):
                    #     print("{}-> it {} update min = {}".format("-"*(iteration*3), iteration, m))
        # nextSeq+=minSeq
        nextSeqLen+=m
        # print("<={} it {} : min found options {}".format("="*(iteration*3), iteration, nextSeq))
        curPos=digits[se]
    # print("it {} nextSeq = {}".format(iteration, nextSeq))
    # seen["{},{}".format(seq, iteration)]=nextSeq
    seen["{},{}".format(seq, iteration)]=nextSeqLen
    # return nextSeq
    return nextSeqLen

# 68 * 29  --> <<vAA>A^>A<A>vAA^A<<vA>>^AvA^A<<vA>>^AA<vA>A^A<A>A<<vA>A^>AAA<A>vA^A
# 029A:        <vA<AA>>^AvAA<^A>A<v<A>>^AvA^A<vA>^A<v<A>^A>AAvA^A<v<A>A>^AAAvA<^A>A

# 60 * 980 --> <<vA>>^AAAvA^A<<vAA>A^>A<A>vAA^A<<vA>A^>AAA<A>vA^A<vA>^A<A>A
# 980A: <v<A>>^AAAvA^A<vA<AA>>^AvAA<^A>A<v<A>A>^AAAvA<^A>A<vA>^A<A>A

# 76 * 179 --> <<vAA>A^>A<A>vA^A<vA<A^>>A<A>vAA^A<<vA>>^AAvA^A<vA>^AA<A>A<<vA>A^>AAA<A>vA^A
# 179A: <v<A>>^A<vA<A>>^AAvAA<^A>A<v<A>>^AAvA^A<vA>^AA<A>A<v<A>A>^AAAvA<^A>A

# 74 * 456 --> <<vAA>A^>A<A>vA^A<vA<A^>>A<A>vA^AvA^A<vA>^A<A>A<vA>^A<A>A<<vA>A^>AA<A>vA^A
# 456A: <v<A>>^AA<vA<A>>^AAvAA<^A>A<vA>^A<A>A<vA>^A<A>A<v<A>A>^AAvA<^A>A

# 64 * 379 --> <<vA>>^AvA^A<<vAA>A^>AA<A>vA^AAvA^A<vA>^AA<A>A<<vA>A^>AAA<A>vA^A
# 379A: <v<A>>^AvA^A<vA<AA>>^AAvA<^A>AAvA^A<vA>^AA<A>A<v<A>A>^AAAvA<^A>A



# PART ONE
count = 0
res=[]
for i, c in enumerate(codes):
    print(''.join(dg[i]))
    seq=getseq(''.join(dg[i]),0,0)
    # res.append(str(len(seq)*c))
    res.append(str(seq*c))
    # print("{} --> {}".format(digits[i], seq))
    # print("{} * {} --> {}".format(len(seq),c, seq))
    # print("{} * {}".format(len(seq),c))
    # count+=len(seq)*c
    count+=seq*c
print("{};{}".format(depth,';'.join(res)))

# <<vA<<vA<vAAA<<vAAA<vAA<<vAA<<vAAA<<vA<vAA<<vA<vAA<<vA<vAAA
# <vA<AA>>^AvAA<^A>A<v<A>>^AvA^A<vA>^A<v<A>^A>AAvA^A<v<A>A>^AAAvA<^A>A

# PART TWO
count2 = 0

# PART ONE
print("PART ONE : count = {}".format(count))
# 141636 KO
# 143536 KO
# 136100 KO
# 134904 ???
# 136780 OK !!!!


# PART TWO
print("PART TWO : count2 = {}".format(count2))
# 102131567655792 too Low
# 102131567707638 not good ?????
# 167538833832712 OKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKK !!!!!!!!!!!!!!!!
# 228657032675066 not good
# 245793404742406 not good

# 248691843924447 too High
# 248691844634036 too High ???

endTime=time.time()
print("Process time spent : {}s".format(round(endTime-startTime,2)))
