import sys

lines = [line.strip() for line in open(sys.argv[1]).readlines()]

dim = 1000

grid = [[0]*dim for i in range(dim)]

for x in range(dim):
    row = []
    for y in range(dim):
        row.append(0)
    grid.append(row)

for line in lines:
    fields = line.split()
    x1,y1 = [int(i) for i in fields[0].split(',')]
    x2,y2 = [int(i) for i in fields[2].split(',')]

    if x1 == x2:
        s = min(y1,y2)
        f = max(y1,y2)
        for i in range(s,f+1):
            grid[i][x1] += 1
    elif y1 == y2:
        s = min(x1,x2)
        f = max(x1,x2)
        for i in range(s,f+1):
            grid[y1][i] += 1
    else:
        xdir = 0
        if x1 > x2:
            xdir = -1
        else:
            xdir = 1

        ydir = 0
        if y1 > y2:
            ydir = -1
        else:
            ydir = 1

        for i in range(abs(x1-x2) + 1):
            grid[y1][x1] += 1
            x1 += xdir
            y1 += ydir

total = 0
for i in range(dim):
    for j in range(dim):
        if grid[i][j] > 1:
            total += 1

print(total)
