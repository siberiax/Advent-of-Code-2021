import sys
import networkx as nx
from networkx.algorithms.shortest_paths.weighted import single_source_dijkstra

lines = [line.strip() for line in open(sys.argv[1]).readlines()]

l = len(lines)
dim = len(lines) * 5

grid = [[0]*dim for i in range(dim)]

for row in range(len(grid)):
    for col in range(len(grid)):
        if row < l and col < l:
            grid[row][col] = int(lines[row][col])
        elif row >= l:
            el = grid[row-l][col] + 1
            if el == 10:
                el = 1
            grid[row][col] = el
        else:
            el = grid[row][col-l] + 1
            if el == 10:
                el = 1
            grid[row][col] = el

G = nx.DiGraph()

for row in range(dim + 2):
    for col in range(dim + 2):
        G.add_node((row,col))

for row in range(1, dim+1):
    for col in range(1, dim+1):
        w = grid[row-1][col-1]

        nbrs = [(-1,0), (0,-1), (0,1), (1,0)]
        for r,c in nbrs:
            G.add_edge((row+r, col+c), (row,col), weight=w)

print(single_source_dijkstra(G, (1,1), (dim,dim))[0])
