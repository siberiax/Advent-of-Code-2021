import sys
from copy import deepcopy

lines = [line.strip() for line in open(sys.argv[1]).readlines()]

grid = []
for line in lines:
    row = []
    for c in line:
        row.append(int(c))
    grid.append(row)

bordered = [[11] * (len(grid[0]) + 2)]
for row in grid:
    bordered.append([11] + row + [11])
bordered.append([11] * (len(grid[0]) + 2))

grid = bordered

total_flashes = 0
not_all = False
flashes100 = 0
steps = 0
while not not_all:
    steps += 1
    gridc = deepcopy(grid)
    flashed = []
    seen = set()
    for row in range(1, len(grid)-1):
        for col in range(1, len(grid[0])-1):
            gridc[row][col] += 1
            if gridc[row][col] == 10:
                flashed.append((row,col))
                seen.add((row,col))

    while len(flashed):
        new_flashes = []
        for row, col in flashed:
            total_flashes += 1
            neighbs = [(-1,-1), (-1,0), (-1, 1), (0,1), (0,-1), (1,-1), (1,0), (1,1)]
            for r,c in neighbs:
                if gridc[row-r][col-c] != 11 and (row-r, col-c) not in seen:
                    gridc[row-r][col-c] += 1
                    if gridc[row-r][col-c] == 10:
                        flashed.append((row-r,col-c))
                        seen.add((row-r,col-c))

        flashed = new_flashes

    for row, col in seen:
        gridc[row][col] = 0

    grid = deepcopy(gridc)

    all_zero = True
    for row in range(1, len(grid)-1):
        for col in range(1, len(grid[0])-1):
            if grid[row][col]:
                all_zero = False
                break

    if steps == 100:
        flashes100 = total_flashes

    if all_zero:
        not_all = True


print(flashes100)
print(steps)
