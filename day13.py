import sys

lines = [line.strip() for line in open(sys.argv[1]).readlines()]

coords = []
folds = []
fold = False
maxy = 0
maxx = 0
for line in lines:
    if not line:
        fold = True
        continue
    if fold:
        fields = line.split()[-1].split('=')
        if not maxy and fields[0] == 'y':
            maxy = int(fields[1])
        if not maxx and fields[0] == 'x':
            maxx = int(fields[1])
        folds.append((fields[0], int(fields[1])))
    else:
        coords.append(line.split(','))

grid = [[0]*(maxx*2+1) for i in range(maxy*2+1)]

for coord in coords:
    col,row = [int(i) for i in coord]
    grid[row][col] = 1

for fold in folds:
    new_grid = []
    if fold[0] == 'x':
        for row in range(len(grid)):
            r = []
            for col in range(fold[1]):
                r.append(grid[row][col] + grid[row][-(col+1)])
            new_grid.append(r)
    else:
        for row in range(fold[1]):
            r = []
            for col in range(len(grid[0])):
                r.append(grid[row][col] + grid[-(row+1)][col])
            new_grid.append(r)
    grid = new_grid

    total = 0
    for row in grid:
        for col in row:
            if col:
                total += 1

for row in grid:
    r = ""
    for col in row:
        if col:
            r += '#'
        else:
            r += ' '
    print(r)
