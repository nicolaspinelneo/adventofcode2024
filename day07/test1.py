import re
import copy
import time

startTime=time.time()

file1 = open('./2024/day07/testpyfile2.csv', 'r')
Lines = file1.readlines()


# matrice=[]

# PART ONE
# linear solution
def equOk(valExpected, numb):
    for i in range(2 ** (len(numb)-1)):
        # print(i)
        bin=i
        valComputed=numb[0]
        for j in range(len(numb)-1):
            if(bin%2==0):
                # print("+")
                valComputed+=numb[j+1]
            else:
                # print("*")
                valComputed*=numb[j+1]
            bin=bin//2
        if valComputed==valExpected:
            return True
    return False

# recursive solution
def equOkReq(valExpected, valComputed, numb):
    if(len(numb)==0):
        return valExpected==valComputed
    else:
        return equOkReq(valExpected, valComputed+numb[0], numb[1:]) or equOkReq(valExpected, valComputed*numb[0], numb[1:])

# PART TWO
# linear solution
def equOk2(valExpected, numb):
    for i in range(3 ** (len(numb)-1)):
        # print(i)
        bin=i
        valComputed=numb[0]
        for j in range(len(numb)-1):
            if(bin%3==0):
                # print("+")
                valComputed+=numb[j+1]
            elif(bin%3==1):
                # print("*")
                valComputed*=numb[j+1]
            else:
                # valComputed=valComputed*10*len(str(numb[j+2]))+numb[j+2]
                valComputed=valComputed*(10**len(str(numb[j+1])))+numb[j+1]
            bin=bin//3
        if valComputed==valExpected:
            # bin=i
            # sol=str(numb[0])
            # for j in range(len(numb)-1):
            #     if(bin%3==0):
            #         sol+=" + "+str(numb[j+1])
            #     elif(bin%3==1):
            #         sol+=" * "+str(numb[j+1])
            #     else:
            #         sol+=" | "+str(numb[j+1])
            #     bin=bin//3
            # print(sol)
            return True
    return False

# recursive solution
def equOkReq2(valExpected, valComputed, numb):
    # print("valExpected : {}, valComputed : {}, numb : {}".format(valExpected, valComputed, numb))
    if(len(numb)==0):
        return valExpected==valComputed
    else:
        return equOkReq2(valExpected, valComputed+numb[0], numb[1:]) or equOkReq2(valExpected, valComputed*numb[0], numb[1:]) or equOkReq2(valExpected, valComputed*(10**len(str(numb[0])))+numb[0], numb[1:])

count = 0
count2 = 0
for line in Lines:
    line=line.strip()
    print(line)
    # matrice.append(line)
    allNumbers = re.findall(r'\d+', line)
    allNumbers=[int(x) for x in allNumbers]
    # if(equOk(allNumbers[0], allNumbers[1:])):
    #     print("ok {}:{}".format(allNumbers[0],allNumbers[1:]))
    #     count+=allNumbers[0]
    if(equOkReq(allNumbers[0], allNumbers[1], allNumbers[2:])):
        # print("ok1 {}:{}".format(allNumbers[0],allNumbers[1:]))
        count+=allNumbers[0]
    # if(equOk2(allNumbers[0], allNumbers[1:])):
    #     # print("ok2 {}:{}".format(allNumbers[0],allNumbers[1:]))
    #     count2+=allNumbers[0]
    if(equOkReq2(allNumbers[0], allNumbers[1], allNumbers[2:])):
        # print("ok2REQ {}:{}".format(allNumbers[0],allNumbers[1:]))
        count2+=allNumbers[0]

    
# PART ONE
print("PART ONE : count = {}".format(count))
# 1582598718861

# PART TWO
print("PART TWO : count2 = {}".format(count2))
# 165278151522644

endTime=time.time()
print("Process time spent : {}s".format(round(endTime-startTime,2)))
