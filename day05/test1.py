import re
import copy

file1 = open('./2024/day05/testpyfile2.csv', 'r')
Lines = file1.readlines()

# def func(param):
#     return False
    
# matrice=[]
pagesOrder=[]
pagesToPrint=[]
firstPart=True
for line in Lines:
    line=line.strip()
    if(firstPart and line!=""):
        allNumbers = re.findall(r'\d+', line)
        allNumbers=[int(x) for x in allNumbers]
        pagesOrder.append(allNumbers)
    elif(line==""):
        firstPart=False
    else:
        allNumbers = re.findall(r'\d+', line)
        allNumbers=[int(x) for x in allNumbers]
        pagesToPrint.append(allNumbers)
    # print(line)

# print(pagesOrder)
# print(pagesToPrint)

def correctOrder(page, order):
    for a in range(len(page)-1):
        for b in range(a+1, len(page)):
            if [page[b], page[a]] in order:
                return False
    return True

def middleReordered(page, order):
    for a in range(len(page)-1):
        for b in range(a+1, len(page)):
            if [page[b], page[a]] in order:
                swap=page[b]
                page[b]=page[a]
                page[a]=swap
    # print(page)
    # print("correct order now ? {}".format(correctOrder(page, pagesOrder)))
    return page[len(page)//2]

# PART ONE
count = 0
# PART TWO
count2 = 0
for i in range(len(pagesToPrint)):
    if(correctOrder(pagesToPrint[i], pagesOrder)):
        # print("{} in correctOrder".format(pagesToPrint[i]))
        count+=pagesToPrint[i][len(pagesToPrint[i])//2]
    else:
        # print("{} not in correctOrder".format(pagesToPrint[i]))
        count2+=middleReordered(pagesToPrint[i], pagesOrder)
        # print("{} middleReordered".format(middleReordered(pagesToPrint[i], pagesOrder)))
        
    
# PART ONE
print("PART ONE : count = {}".format(count))
# 5064

# PART TWO
print("PART TWO : count2 = {}".format(count2))
# 5152