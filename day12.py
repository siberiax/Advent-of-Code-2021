import sys
from collections import defaultdict
from copy import deepcopy

def maxLower(path, next):
    if next.isupper():
        return False
    visited_twice = False
    for node in path:
        if node.islower() and path.count(node) > 1:
            visited_twice = True
    if not visited_twice:
        return False
    else:
        return next in path

lines = [line.strip() for line in open(sys.argv[1]).readlines()]

graph = defaultdict(list)

for line in lines:
    fields = line.split('-')
    graph[fields[0]].append(fields[1])
    graph[fields[1]].append(fields[0])

complete = []
curr = [['start']]

while len(curr):
    new_curr = []
    for el in curr:
        end = el[-1]
        for neighb in graph[end]:
            if neighb == 'end':
                complete.append(el)
            elif neighb == 'start' or maxLower(el, neighb):
                continue
            else:
                cop = deepcopy(el)
                cop.append(neighb)
                new_curr.append(cop)
    curr = new_curr

complete.sort()

print(len(complete))
