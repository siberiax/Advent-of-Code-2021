import sys
from collections import defaultdict

lines = [line.strip() for line in open(sys.argv[1]).readlines()]

input = lines[0]
start = input[0]
curr = defaultdict(int)

for i in range(len(input)-1):
    curr[input[i] + input[i+1]] += 1

polymers = {}

for line in lines[2:]:
    k,v = line.split(' -> ')
    polymers[k] = v

iterations = 40

for _ in range(iterations):
    new = defaultdict(int)
    for key in curr.keys():
        poly = polymers[key]
        new[key[0] + poly] += 1*curr[key]
        new[poly + key[1]] += 1*curr[key]

    curr = new

l2c = defaultdict(int)
l2c[start] = 1
for key, v in curr.items():
    l2c[key[1]] += v

occurences = list(l2c.values())
occurences.sort()

print(l2c)

print(occurences[-1] - occurences[0])
