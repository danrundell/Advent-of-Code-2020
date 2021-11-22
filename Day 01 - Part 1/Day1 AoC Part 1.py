v = []

with open('aoc1data.txt') as k:
    v = k.readlines()

v = list(map(int, v))
ylist = v

print(ylist) 
target = 2020 
for i in range(len(ylist)):
    sno = target-ylist[i]
    for j in range(i+1, len(ylist)):
        if ylist[j] == sno:
            print(ylist[i])
            print(ylist[j])
            print(ylist[i]*ylist[j])
            
open('aoc1data.txt').close()
