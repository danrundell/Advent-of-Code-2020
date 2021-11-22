x = [int(y) for y in open('aoc1data.txt').readlines()]
for i in range(0,len(x)):
    for j in range(1,len(x)):
        for k in range (2, len(x)):
            if x[i] + x[j] + x[k] == 2020:
                print(x[i]*x[j]*x[k])
