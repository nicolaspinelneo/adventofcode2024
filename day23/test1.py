import re
import copy
import time
import math

# import sys
# sys.setrecursionlimit(15000)

startTime=time.time()

file1 = open('./2024/day23/testpyfile2.csv', 'r')
Lines = file1.readlines()

net=[]
for l, line in enumerate(Lines):
    line=line.strip()
    # print(line)
    net.append(line.split("-"))
    # allNumbers = re.findall(r'\d+', line)
    # allNumbers=[int(x) for x in allNumbers]

# print(net)
# G = [int(row) for row in line]
# G = [[c for c in row] for row in matrice]
# G2 = [[c for c in row] for row in matrice]
# G3 = [[c for c in row] for row in matrice]

# dir=[[0,1],[1,0],[0,-1],[-1,0]]
listcpt={}
for n in net:
    for i in [0,1]:
        if not n[i] in listcpt:
            listcpt[n[i]]=[n[(i+1)%2]]
        else:
            listcpt[n[i]].append(n[(i+1)%2])

# PART ONE
count = 0

net3=[]
for n1 in range(len(listcpt.keys())):
    cpt1=list(listcpt.keys())[n1]
    if cpt1[0]=="t":
    # if True:
        # print(k, listcpt[k])
        for c1 in range(len(listcpt[cpt1])-1):
            for c2 in range(1,len(listcpt[cpt1])):
                cpt2=listcpt[cpt1][c1]
                cpt3=listcpt[cpt1][c2]
                if [cpt2,cpt3] in net or [cpt3,cpt2] in net:
                    if not([cpt1, cpt2, cpt3] in net3 or [cpt1, cpt3, cpt2] in net3 or [cpt2, cpt1, cpt3] in net3 or [cpt2, cpt3, cpt1] in net3 or [cpt3, cpt1, cpt2] in net3 or [cpt3, cpt2, cpt1] in net3):
                        # add it if not already exists
                        net3.append([cpt1, cpt2, cpt3])
                        # print(cpt1,cpt2,cpt3)
                        count+=1
                    # break


# print(listcpt.keys())



# net3=[]
# for n1 in range(len(listcpt.keys())-1):
#     for n2 in range(n1+1,len(listcpt.keys())):
#         cpt1 = list(listcpt.keys())[n1]
#         cpt2 = list(listcpt.keys())[n2]
#         # is common pc between n1 and n2
#         if "t" in cpt1 or "t" in cpt2:
#             for cpt3 in listcpt[cpt1]:
#                 if cpt3 in listcpt[cpt2]:
#                     # found new 3 some network
#                     if not([cpt1, cpt2, cpt3] in net3 or [cpt1, cpt3, cpt2] in net3 or [cpt2, cpt1, cpt3] in net3 or [cpt2, cpt3, cpt1] in net3 or [cpt3, cpt1, cpt2] in net3 or [cpt3, cpt2, cpt1] in net3):
#                         # add it if not already exists
#                         net3.append([cpt1, cpt2, cpt3])
#                         print(cpt1,cpt2,cpt3)
#                         count+=1
#                     break
#     for n2 in listcpt:
#         # if [n[0], n2] in net or [n2, n[0]] in net or [n[1], n2] in net or [n2, n[1]] in net:
#         if [n[0], n2] in net:
#             net3.append([n[0], n[1], n2])
# print(net3)


# PART TWO
count2 = 0

# for n1 in range(len(listcpt.keys())):
#     cpt1=list(listcpt.keys())[n1]
#     print(cpt1, listcpt[cpt1])

for n in net3:
    print(n)


# PART ONE
print("PART ONE : count = {}".format(count))
# 1405 KO
# 2351 KO
# 1323 OK

# PART TWO
print("PART TWO : count2 = {}".format(count2))


endTime=time.time()
print("Process time spent : {}s".format(round(endTime-startTime,2)))
