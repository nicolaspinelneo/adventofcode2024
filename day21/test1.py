import re
import copy
import time
import math

# import sys
# sys.setrecursionlimit(15000)

startTime=time.time()

file1 = open('./2024/day21/testpyfile2.csv', 'r')
Lines = file1.readlines()

matrice=[]
codes=[]
digits=[]
for l, line in enumerate(Lines):
    line=line.strip()
    # print(line)
    # allNumbers = re.findall(r'\d+', line)
    # allNumbers=[int(x) for x in allNumbers]
    matrice.append(line)


    allNumbers = re.findall(r'\d+', line)
    codes.append(int(allNumbers[0]))
    digits.append([d for d in line])
    # allNumbers=[int(x) for x in allNumbers]
# G = [int(row) for row in line]
G = [[c for c in row] for row in matrice]
# G2 = [[c for c in row] for row in matrice]
# G3 = [[c for c in row] for row in matrice]

dir=[[0,1],[1,0],[0,-1],[-1,0]]

#     +---+---+
#     | ^ | A |
# +---+---+---+
# | < | v | > |
# +---+---+---+

# +---+---+---+
# | 7 | 8 | 9 |
# +---+---+---+
# | 4 | 5 | 6 |
# +---+---+---+
# | 1 | 2 | 3 |
# +---+---+---+
#     | 0 | A |
#     +---+---+

# 029A: <vA<AA>>^AvAA<^A>A<v<A>>^AvA^A<vA>^A<v<A>^A>AAvA^A<v<A>A>^AAAvA<^A>A
#         v <<   A >>  ^ A   A   A > A  v  A  

# <<vA A>A>^AAvA<^ A> Av A^A<<vA>>^AAvA^A<vA>^AA<A>A<<vA>A>^AAAvA<^A>A
#    < < v  AA >   ^  A  > A...
#           <<        ^    A
#                          1

# <v<A>>^A<vA<A>>^AAvAA<^A>A<v<A>>^AAvA^A<vA>^AA<A>A<v<A>A>^AAAvA<^A>A
#    <   A  v <   AA >>  ^ A...
#        ^        <<       A

# <<vAA>A>^AAvA<^A>AAv    A^A<vA>^A<A>A<vA>^A<A>A<<vA>A>^AAvA<^A>A
    #  << v  AA >  ^ AA
    #        <<      ^^
    #                       4

# <v<A>>^AA<vA<A>>^AAvAA<^A>A<vA>^A<A>A<vA>^A<A>A<v<A>A>^AAvA<^A>A
    #  <   AA  v <   AA >>  ^ A
    #      ^^        <<       A

def allCombine(nb,tablesize):
    print("allCombine {} on {}".format(nb,tablesize))
    nbCombine=0
    tnb=[i for i in range(nb)]

    end=False
    while(not end):
        nbCombine+=1
        # compute next
        if(len(tnb)>0 and tnb[0]<tablesize-nb):
            idtomove=nb-1
            foundidtomove=False
            while(not foundidtomove):
                if tnb[idtomove]<tablesize-nb+idtomove:
                    foundidtomove=True
                    tnb[idtomove]+=1
                    for rest in range(idtomove+1, nb):
                        tnb[rest]=tnb[idtomove]+rest-idtomove
                else:
                    idtomove-=1
        else:
            end=True
    print(nbCombine)

def recCombi(str):
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
        return combi

def getAllDiffCombi(stoadd):
    listeCombi=recCombi(stoadd)

    return listeCombi

direc={">":[1,0],
       "<":[-1,0],
       "v":[0,1],
       "^":[0,-1]}

seen={}
nbSeq=0
def getseq(seq, iteration):
    global seen
    global nbSeq
    nbSeq+=1
    # if(nbSeq%2==0):
    #     print("nbSeq : {} -> {}".format(nbSeq, ''.join(seq)))
    if "{},{}".format(seq, iteration) in seen:
        return seen["{},{}".format(seq, iteration)]
    s=[""]
    if(iteration==0):
        digits={
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
    else:
        digits={
            '^':[1,0],
            'A':[2,0],
            '<':[0,1],
            'v':[1,1],
            '>':[2,1]
        }
    curPos=digits["A"] # A
    # print("iter{} from A".format(iteration))
    for se in seq:
        goto=digits[se]
        stoadd=""
        # print("iter{} to {}".format(iteration,se))

        # for i, dir in enumerate([["v","^"],[">", "<"]]):
        # for i, dir in enumerate([[">", "<"],["v","^"]]):
        for i, dir in enumerate([[">", "<"],["v","^"]]):
            if(curPos[i]<goto[i]):
                stoadd+=dir[0]*abs(curPos[i]-goto[i])
            elif(curPos[i]>goto[i]):
                stoadd+=dir[1]*abs(curPos[i]-goto[i])
        # on cherche toutes les combinaisons
        comb=getAllDiffCombi(stoadd)
        # check if not forbidden position for each combi
        autorizedComb=[]
        for c in comb:
            curPosCheck=copy.copy(curPos)
            forbidden=False
            for d in c:
                curPosCheck=[curPosCheck[0]+direc[d][0],curPosCheck[1]+direc[d][1]]
                if iteration==0 and curPosCheck==[0,3]:
                    #forbidden
                    forbidden=True
                    break
                # if iteration>0 and curPosCheck==[0,0]:
                #     #forbidden
                #     forbidden=True
                #     break
            if not forbidden:
                autorizedComb.append(c)

        comb=copy.copy(autorizedComb)

        if(iteration>0):
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

        # if(iteration==0 and curPos==[2,3] and goto==[0,2]):
        #     comb.remove("<<^")
        # elif(iteration==0 and curPos==[2,3] and goto==[0,1]):
        #     comb.remove("<<^^")
        # elif(iteration==0 and curPos==[2,3] and goto==[0,0]):
        #     comb.remove("<<^^^")
        # elif(iteration==0 and curPos==[1,3] and goto==[0,2]):
        #     comb.remove("<^")
        # elif(iteration==0 and curPos==[1,3] and goto==[0,1]):
        #     comb.remove("<^^")
        # elif(iteration==0 and curPos==[1,3] and goto==[0,0]):
        #     comb.remove("<^^^")
        # elif(iteration>0 and curPos==[2,0] and goto==[0,1]):
        #     comb.remove("<<v")
        # elif(iteration>0 and curPos==[2,1] and goto==[0,1]):
        #     comb.remove("<v")
        # print("nb combi = {}".format(len(comb)))
        # duplique s par le nombre de combinaisons
        nbBefore=len(s)
        for idComb in range(len(comb)-1):  # to put back !!!!
            for ss in range(nbBefore):
                s.append(s[ss])
        for ss in range(len(s)):
            s[ss]+=comb[ss%len(comb)]+"A"
        # s+=stoadd+"A"
        curPos=digits[se]
    m=-1
    mins=""
    # if(iteration<1+0): #  0.02s
    if(iteration<2+0): # 0.89
    # if(iteration<2+10): # 51.57s
    # if(iteration<2+24): # ??
        for ss in s:
            if(m==-1):
                mins = getseq([d for d in ss],iteration+1)
                m=len(mins)
            else:
                new = getseq([d for d in ss],iteration+1)
                if len(new)<m and len(new)>0:
                    mins=new
                    m=len(new)
    else:
        for ss in s:
            if(m==-1):
                m=len(ss)
                mins=ss
            else:
                m=min(len(ss), m)
                mins=ss
        # print(m)
    # print(mins)
    seen["{},{}".format(seq, iteration)]=mins
    return mins

# PART ONE
count = 0
for i, c in enumerate(codes):
    seq=getseq(digits[i],0)
    # print("{} --> {}".format(digits[i], seq))
    # print("{} * {} --> {}".format(len(seq),c, seq))
    count+=len(seq)*c



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
# ???


# bSym 4760 for iteration 7860

endTime=time.time()
print("Process time spent : {}s".format(round(endTime-startTime,2)))
