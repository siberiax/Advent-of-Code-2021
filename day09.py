import sys

lines = [line.strip() for line in open(sys.argv[1]).readlines()]

grid = []
for line in lines:
    row = []
    for c in line:
        row.append(int(c))
    grid.append(row)

bordered = [[10] * (len(grid[0]) + 2)]
for row in grid:
    bordered.append([10] + row + [10])
bordered.append([10] * (len(grid[0]) + 2))

grid = bordered

total = 0
bottoms = []
for row in range(1, len(grid)-1):
    for col in range(1, len(grid[0])-1):
        curr = grid[row][col]
        nbrs = [grid[row-1][col], grid[row][col-1], grid[row][col+1], grid[row+1][col]]
        if all(curr < n for n in nbrs):
            total += curr + 1
            bottoms.append((row,col))

print(total)

sizes = []
for bottom in bottoms:
    size = 0
    seen = set()
    seen.add(bottom)
    to_check = [bottom]
    while len(to_check):
        next = []
        for point in to_check:
            size += 1
            row, col = point
            nbrs = [(1,0), (0,1), (0,-1), (-1,0)]
            for nbr in nbrs:
                r, c = nbr
                if grid[row+r][col+c] < 9 and (row+r, col+c) not in seen:
                    seen.add((row+r, col+c))
                    next.append((row+r, col+c))
        to_check = next
    sizes.append(size)

sizes.sort()

print(sizes[-1] * sizes[-2] * sizes[-3])
