import re
import copy

file1 = open('./2024/day03/testpyfile.csv', 'r')
Lines = file1.readlines()

# def func(param):
#     return False
    
count=0
matrice=[]
for line in Lines:
    line=line.strip()
    print(line)
    # premiere partie de la chaine
    print(line[:len(line)//2])
    # deuxième partie de la chaine
    print(line[len(line)//2:])
    matrice.append(line)
    # matrice de nombres
    allNumbers = re.findall(r'\d+', line)
    allNumbers=[int(x) for x in allNumbers]
    print(allNumbers)

# matrice de caractères
G = [[c for c in row] for row in matrice]
print(G)


# PART ONE
# ???
print("count = {}".format(count))

# PART TWO
# ???
print("count = {}".format(count))
