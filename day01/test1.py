import re

file1 = open('./2024/day01/testpyfile.csv', 'r')
Lines = file1.readlines()

count = 0
sum = 0
# Strips the newline character
elfCalories=[]
elfCalories.append(0)
nbElf=1
maxCal=0

for line in Lines:
    count += 1
    line=line.strip()
    if(line==""):
        nbElf+=1
        elfCalories.append(0)
        print("next elf")
    else:
        print("add {} to current elf".format(int(line)))
        elfCalories[-1]+=int(line)
        print("compare {} to {}".format(elfCalories[-1], maxCal))
        if(elfCalories[-1]>maxCal):
            print("compare {} > {}".format(elfCalories[-1], maxCal))
            maxCal=elfCalories[-1]

    print("Line {}: <- {}".format(count, line.strip()))
    sum+=count

print("NbElves {}".format(nbElf))
print(elfCalories)
print("maxCal {}".format(maxCal))
print(sum)