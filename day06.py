import sys
from collections import defaultdict

lines = [line.strip() for line in open(sys.argv[1]).readlines()]
nums = [int(i) for i in lines[0].split(',')]

iterations = 80

its = defaultdict(int)
for n in nums:
    its[n] += 1

total = len(nums)
for i in range(iterations):
    total += its[i]
    its[i+7] += its[i]
    its[i+9] += its[i]

print(total)
